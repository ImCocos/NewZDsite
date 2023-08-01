from pprint import pprint
import django
import os

from django.shortcuts import get_object_or_404

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RZD.settings')
django.setup()

from Stations.models import StationStats, Recirculer, Ticket



st = get_object_or_404(StationStats, name='Останкино')
print(st.pk)