from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
import random
from .forms import *
from .models import *
from .utils import *
import requests
from .config import *




    
def get_self_games(request):
    self_games = Self_game.objects.all()
    return self_games

def index(request):
    if request.method == "POST":
        form = request.POST.get("CruptoAddr", None)
        if form[:2] == "0x":
            prof = Profile.objects.get(user=request.user)
            prof.CruptoAddr = form
            prof.save()
    data = {
        "auth" : 0,
            }
    if request.user.is_authenticated:  # Проверяем, аутентифицирован ли пользователь
        try:
            user_profile = Profile.objects.get(user=request.user)
            basket = list(map(lambda x: int(x.id),list(linkGame.objects.filter(UserId=request.user))))
            lose_count = len(Loto.objects.filter(Winner=request.user)) - len(basket)
            LotoL = list(Game.objects.filter(cat__name="Loto", is_published=True))
            self_games = Self_game.objects.filter(post=1)
            LotoL = list(map(lambda x: {
                "id": int(x.id),
                'stavka': x.stavka,
                "MaxPeople": x.MaxPeople,
                "People":x.People,
                "vsego": x.MaxPeople * x.stavka
            }, LotoL))

            data = {
                "auth" : 1,
                "lose": lose_count,
                "basket": basket,
                "form": {},
                "Profile": user_profile,
                "Games": Loto.objects.filter(Winner=request.user),
                "Loto": LotoL,
                "Self_games": self_games,
            }
        except Profile.DoesNotExist:
            pass

    return render(request, "main/layout.html", context=data)


def about(request):
    return render(request, "main/about.html")


def register(request):
    pass

def create_self_spor(request, description):
    self_spor = Self_game()
    self_spor.owner = request.user
    self_spor.description = description
    self_spor.save()

class CruptoAddr(CreateView):
    form_class = CruptoAddrForm
    template_name = 'main/layout.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        # create_self_spor(self.request, description)
        return redirect('home')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class Create_self_game(CreateView):
    form_class = SelfGameForm
    template_name = 'main/add_new_self_spor.html'
    success_url = reverse_lazy('create_spor')

    def form_valid(self, form):
        form_self_spor = form.save(commit=False)  
               
        description = form_self_spor.description
        create_self_spor(self.request, description)
        return redirect('home')



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/Home/login.html'
    success_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
