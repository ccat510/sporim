# Generated by Django 5.1.2 on 2024-11-01 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_зщые_self_game_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='self_game',
            name='stastavka',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='self_game',
            name='timelimit',
            field=models.IntegerField(default=30, verbose_name='Время ожидания в минутах'),
        ),
        migrations.DeleteModel(
            name='Sporim_self',
        ),
    ]
