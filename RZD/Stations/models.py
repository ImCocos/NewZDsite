from django.db import models


class Ticket(models.Model):
    st_from = models.IntegerField()
    st_to = models.IntegerField()


class Recirculer(models.Model):
    power = models.IntegerField(default=0)


class StationStats(models.Model):
    name = models.TextField()
    people = models.IntegerField(default=0)
    tickets = models.ManyToManyField(Ticket)
    recirculers = models.ManyToManyField(Recirculer)
