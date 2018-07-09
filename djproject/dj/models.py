# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class database_try(models.Model):
    artist=models.CharField(max_length=30)
    usn=models.CharField(max_length=30)

    def __str__(self):
        return self.artist + ' - ' + self.usn

class employee(models.Model):
    usn=models.ForeignKey(database_try,on_delete=models.CASCADE)
    phno=models.CharField(max_length=10)
    desg = models.CharField(max_length=30)
