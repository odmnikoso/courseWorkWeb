# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 09:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.CharField(max_length=250, verbose_name='Описание')),
                ('body', models.TextField(verbose_name='Содержание')),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('like', models.IntegerField(default=0, verbose_name='Нравиться')),
                ('viewing', models.IntegerField(default=0, verbose_name='Просмотрено')),
                ('status', models.CharField(choices=[('d', 'Черновик'), ('p', 'Опубликовано'), ('w', 'В корзине')], max_length=1, verbose_name='Статус')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('list_users_like', models.ManyToManyField(blank=True, null=True, related_name='news_list_users_like', to=settings.AUTH_USER_MODEL, verbose_name='Список пользователей, которым нравится новость')),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
