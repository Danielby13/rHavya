# Generated by Django 3.1 on 2020-08-27 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(default='member', max_length=100),
        ),
    ]
