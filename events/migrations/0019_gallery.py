# Generated by Django 3.1 on 2020-09-06 11:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_auto_20200902_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('event_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(default='default.jpeg', upload_to='gallery')),
            ],
        ),
    ]
