from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Month(models.Model):
    owner = models.ForeignKey(User, null = True)

    month = models.IntegerField(default=date.today().month)
    year = models.IntegerField(default=date.today().month)

    def __str__(self):
        return str(self.year)+" "+str(self.month)+" "+str(1)

class Task(models.Model):
    text = models.TextField(default="")
    date = models.TextField(default="")
    owner = models.ForeignKey(User, null = True)


    #mounth = models.ForeignKey(Month, default=None)

    def __str__(self):
        return self.text
