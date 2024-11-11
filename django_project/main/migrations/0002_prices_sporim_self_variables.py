# Generated by Django 5.1.2 on 2024-10-23 08:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stavka', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sporim_self',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Game', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.game')),
                ('Winner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='variables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField(default='Описание', verbose_name='Описание')),
                ('Game', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.game')),
            ],
            options={
                'verbose_name': 'Свой спор',
                'verbose_name_plural': 'Свои споры',
                'ordering': ['id'],
            },
        ),
    ]