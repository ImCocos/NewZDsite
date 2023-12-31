# Generated by Django 4.2.4 on 2023-08-29 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recirculer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_from', models.IntegerField()),
                ('st_to', models.IntegerField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2023, 8, 29, 14, 5, 16, 154664))),
            ],
        ),
        migrations.CreateModel(
            name='StationStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('people', models.IntegerField(default=0)),
                ('emergency', models.BooleanField(default=True)),
                ('recirculers', models.ManyToManyField(to='Stations.recirculer')),
                ('tickets', models.ManyToManyField(to='Stations.ticket')),
            ],
        ),
    ]
