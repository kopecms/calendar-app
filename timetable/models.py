from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    text = models.TextField(default="")
    date = models.TextField(default="")
    owner = models.ForeignKey(User, null = True)

    def __str__(self):
        return self.text

class TasksPerDay(models.Model):
    number = models.IntegerField(default = 0)
    date_text = models.TextField(default="")
    date = models.DateField()
    owner = models.ForeignKey(User, null = True)
