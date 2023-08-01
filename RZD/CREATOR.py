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


for s in StationStats.objects.all():
    s.people = 0
    s.save()

