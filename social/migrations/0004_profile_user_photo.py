# Generated by Django 4.2 on 2023-04-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_twitt'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
