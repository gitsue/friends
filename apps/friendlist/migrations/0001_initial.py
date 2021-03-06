# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-15 17:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ManyToManyField(to='users.User')),
            ],
            managers=[
                ('friendmgr', django.db.models.manager.Manager()),
            ],
        ),
    ]
