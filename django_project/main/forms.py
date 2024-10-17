from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


# class AddPostForm(forms.ModelForm):
#     time_create = models.DateTimeField(auto_now_add=True, verbose_name="time_create")
#     is_published = models.BooleanField(default=True, verbose_name="is_published")
#     UserId = models.ForeignKey(UserSporim, on_delete=models.PROTECT, verbose_name="userId")
#     MaxGamers = models.IntegerField(default=100, verbose_name="MaxGamers")
#     Winner = models.IntegerField(default=0, verbose_name="Winner")

#     class Meta:
#         model = Loto
#         fields = ( 'is_published', 'is_published', 'Winner',"MaxGamers")


class CruptoAddrForm(forms.Form):
    CruptoAddr = forms.CharField(label='CruptoAddr', widget=forms.TextInput(attrs={'class': 'form-input'}))



class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = UserSporim
        fields = ('username', 'email', 'password1', 'password2')
        
        
class RegisterLinkGameForm(UserCreationForm):
    Game = models.ForeignKey(Game, on_delete=models.PROTECT, verbose_name="Game")
    UserId = models.OneToOneField(User,on_delete=models.CASCADE, verbose_name="UserId")
    class Meta:
        model = linkGame
        fields = ('Game',"UserId")

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
