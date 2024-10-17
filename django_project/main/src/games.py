from ..models import *


def linkGameAdd(request, id):
    game = Game.objects.get(id=id)
    baskets = linkGame.objects.filter(UserId=request.user, Game=id)
    if not baskets.exists():
        GL = linkGame(UserId=request.user, Game=game)
        GL.save()
        pr = Profile.objects.get(user=request.user)
        if pr.balance - game.stavka < 0:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        pr.balance -= game.stavka
        pr.wins_coins -= game.stavka
        pr.save()
        game.People += 1
        if game.People == game.MaxPeople:
            basketPeople = linkGame.objects.filter(Game=game)
            Winner = random.choice(list(basketPeople)).UserId
            Loto(Game=game, Winner=Winner).save()
            gameA = game
            gameA.People = 0
            gameA.save()
            game.is_published = False
            WinnerPr = Profile.objects.get(user=Winner)
            WinnerPr.wins_coins += (game.MaxPeople * game.stavka)
            WinnerPr.wins_games += 1
            WinnerPr.balance += (game.MaxPeople * game.stavka)
            WinnerPr.save()
        GL.save()
        game.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
