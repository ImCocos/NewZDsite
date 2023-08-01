from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('data-getter/<int:station_pk>', data_getter, name='data-getter'),
    path('data-sender/<int:station_pk>', data_sender, name='data-sender'),
    path('show-info/<int:station_pk>', show_info, name='show-info'),
    path('buy-ticket', buy_ticket, name='buy-ticket'),
]