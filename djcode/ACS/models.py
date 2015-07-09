# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

#class Login_info: handled by Django User

class classroom(models.Model):
    '''
    | id | name | type | capacity | campus |
    | VARCHAR(20) | VARCHAR(20) | VARCHAR(20) | interget | VARCHAR(20) |
    '''
    #id = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20, default = 'classroom')
    capacity = models.IntegerField()
    campus = models.CharField(max_length=20)

class Application(models.Model):
    #class id
    #cl_ID=models.CharField(max_length=20,primary_key=True)
    id = models.CharField(max_length=20, primary_key=True)
    #course id
    cuz_ID=models.CharField(max_length=20)
    # class time save as json
    classTime=models.TextField()
    #class hour
    classHour = models.IntegerField()
    # class capacity
    class_capacity=models.IntegerField()
    #
    campus=models.CharField(max_length=20)
    # teacher id
    teacherID=models.CharField(max_length=20)
# term
#term = models.CharField(max_length=20)
