from typing import Any
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from random import choice


class Tranzactions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tranz_status = models.IntegerField(default=0)
    hash = models.TextField(verbose_name="hash")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(default=0)
    wins_games = models.PositiveIntegerField(default=0)
    wins_coins = models.IntegerField(default=0)
    CruptoAddr = models.TextField(verbose_name="Адрес", default="None")
    def __str__(self):
        return f"title: {self.user} id: {self.id}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except:
        pass


class UserSporim(User, models.Model):
    class Meta:
        verbose_name = 'Пользователь Sporim'
        verbose_name_plural = 'Пользователи Sporim'
        ordering = ['id']


class Color(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", default="Game")
    color = models.CharField(max_length=255)


class Game(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок", default="Game")
    Description = models.TextField(verbose_name="Описание", default="Описание")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")
    MaxPeople = models.IntegerField(default=100)
    People = models.IntegerField(default=0)
    stavka = models.IntegerField(default=100)
    color = models.CharField(max_length=255,default="#FFFFFF")
    timelimit = models.IntegerField(default=30, verbose_name="Время ожидания в минутах")

    def __str__(self):
        return f"title: {self.title} id: {self.id}"

    class Meta:
        verbose_name = "Игра в Sporim"

@receiver(post_save, sender=Game)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print(instance)
        instance.color = choice(bright_colors)
        instance.save()



class Loto(models.Model):
    Game = models.ForeignKey(Game, on_delete=models.CASCADE, default=None)
    Winner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


    def get_absolute_url(self):
        return reverse('Game', kwargs={'ID': self.Game})

    class Meta:
        verbose_name = 'Лото'
        verbose_name_plural = 'Лото'
        ordering = ['id']


class linkGame(models.Model):
    Game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="Игра")
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    class Meta:
        verbose_name = "Связь между играми"




class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
