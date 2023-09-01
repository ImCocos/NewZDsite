import datetime
from django.db import models
from dateutil.relativedelta import relativedelta


class Ticket(models.Model):
    st_from = models.IntegerField()
    st_to = models.IntegerField()
    timestamp = models.DateTimeField(default=datetime.datetime.now() + relativedelta(seconds=30))


class Recirculer(models.Model):
    power = models.FloatField(default=float(0))


class StationStats(models.Model):
    name = models.TextField()
    people = models.IntegerField(default=0)
    tickets = models.ManyToManyField(Ticket)
    recirculers = models.ManyToManyField(Recirculer)
    emergency = models.BooleanField(default=True)

    def set_power(self, power: float = None):
        r = self.recirculers.all()[0]
        if power == None:
            if self.emergency:
                r.power = round(self.people / 137, 3)
            if not self.emergency:
                r.power = 0
        else:
            r.power = round(power, 3)
        r.save()
        self.save()

