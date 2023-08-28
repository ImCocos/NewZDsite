import asyncio
from pprint import pprint
import django
import os
from threading import Thread
import time
from multiprocessing import Process

from django.shortcuts import get_object_or_404

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RZD.settings')
django.setup()

from Stations.models import StationStats, Recirculer, Ticket


stations_names = [
    'Москва-Пассажирская-Смоленская(Белорусский вокзал)',
    'Москва-Товарная-Смоленская',
    'Беговая',
    'Тестовская',
    'Фили',
    'Славянский бульвар',
    'Кунцево',
    'Рабочий Посёлок',
    'Сетунь',
]

for sn in stations_names:
    s = StationStats(name=sn)
    s.save()
    r = Recirculer()
    r.save()
    s.recirculers.add(r)
    s.save()
    print(f'Saved as {s.name} p:{s.people}, r:{r}')

