# Generated by Django 3.1 on 2020-08-24 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20200824_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='type_event',
        ),
    ]
