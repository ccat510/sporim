from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from ..config import *
from ..models import *
from django.db import transaction


def cheak_connect_api_server():
    request_api_server = requests.get("https://api.etherscan.io/api", params=PARAMS).json()
    if request_api_server["status"] != '1' and request_api_server["message"] != "OK":
        return False
    return request_api_server



@transaction.atomic
def cheak_tranzaction(request):
    user_profile = Profile.objects.get(user=request.user)
    user_addr = user_profile.CruptoAddr
    request_api_server = cheak_connect_api_server()
    if request_api_server:
        tranzactionsBD = list(Tranzactions.objects.filter(user=request.user))
        tranzactionsBD = list(map(lambda x: x["hash"],tranzactionsBD))
        result = list(filter(lambda x: x["from"] == addr, list(request_api_server["result"])))
        result = list(filter(lambda x: not (x["hash"] in tranzactionsBD), result))
        result.sort(key=lambda x: int(x["blockNumber"]))
        tr = 0
        for i in result:
            tranzaction = Tranzactions()
            tranzaction.user = request.user
            tranzaction.hash = i['hash']
            tranzaction.tranz_status = i['txreceipt_status']
            tranzaction.save()
            tr += (int(i['value']) // 10 ** 14 - 1)
        user_profile.balance += tr
        user_profile.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))