from django.urls import path, re_path

from .views import *
from .src.games import linkGameAdd
from .src.tranzaction import cheak_tranzaction


urlpatterns = [
    path('', index, name="home"),
    path('about', about),
    path('login/', LoginUser.as_view(), name="login"),
    path('register/', RegisterUser.as_view(), name="register"),
    path('game/<int:id>/', linkGameAdd , name='games'),
    path('updata_balance', cheak_tranzaction, name='updata_balance'),
    path('create_spor/', Create_self_game.as_view(), name='create_spor'),

]
