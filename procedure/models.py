import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm


class Procedure(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    #user = models.ForeignKey(User)
    user = models.CharField(max_length=255)
    blank = True

    def __unicode__(self):
        return self.name


class Step(models.Model):
    procedure = models.ForeignKey(Procedure)
    order = models.IntegerField(default=0)
    description = models.CharField(max_length=255)
    precede = models.ManyToManyField('self', through='Precedence', related_name='preceded', symmetrical=False)

    def __str__(self):
        return self.description


class Precedence(models.Model):
    name = models.CharField(max_length=255)
    precede = models.ForeignKey(Step, related_name='precedence-precede')
    preceded1 = models.ForeignKey(Step, related_name='precedence-preceded')

    def __str__(self):
        return self.name
