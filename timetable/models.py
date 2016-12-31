from __future__ import unicode_literals

from django.db import models

from datetime import date
# Create your models here.

class Month(models.Model):
    month = models.IntegerField(default=date.today().month)
    year = models.IntegerField(default=date.today().month)

    def __str__(self):
        return str(self.year)+" "+str(self.month)+" "+str(1)

class Task(models.Model):
    pass
