# Generated by Django 4.2 on 2023-04-04 20:27

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='update',
            field=models.DateTimeField(auto_now=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]