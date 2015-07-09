from django.db import models
import datetime


# Create your models here.
class Homework(models.Model):
    '''
    | homework_num | title | content | start_date | end_date |
    |---|---|---|---|---|
    | CHARACTER(8) | VARCHAR(20) | VARCHAR(100) | DATETIME(TEXT) | DATETIME(TEXT) |
    '''
    course_id = models.CharField(max_length = 8)
    title = models.CharField(max_length = 20)
    content = models.CharField(max_length = 100)
    start_date = models.DateTimeField(default = datetime.datetime.now())
    end_date = models.DateTimeField(default = datetime.datetime.now())


class HomeworkFile(models.Model):
    '''
    | homework_num | homework_address |
    |---|---|
    | CHARACTER(8) | VARCHAR(100) |
    '''
    homework_id = models.CharField(max_length = 8, primary_key=True)        
    homework_num = models.CharField(max_length = 8)
    course_id = models.CharField(max_length = 8)
    student_id = models.CharField(max_length = 8)
    homework_add = models.CharField(max_length = 100)
    date = models.DateTimeField(default = datetime.datetime.now())


class Resource(models.Model):
    '''
    | resource_num | resource_add | date | frequency |
    |---|---|---|---|
    | CHARACTER(8) | VARCHAR(100) | DATETIME(TEXT) | INTEGER |
    '''
    course_id = models.CharField(max_length = 8)
    resource_name = models.CharField(max_length = 20)
    resource_add = models.CharField(max_length = 100)
    resource_top = models.CharField(max_length = 20)
    date = models.DateTimeField(default = datetime.datetime.now())
    frequency = models.IntegerField(default = 0)

class Notice(models.Model):
    '''
    | notice_num | content | date |
    |---|---|---|
    | CHARACTER(8) | VARCHAR(100) | DATETIME(TEXT) |
    '''
    notice_num = models.CharField(max_length = 8, primary_key = True)
    notice_title = models.CharField(max_length = 100)
    course_id = models.CharField(max_length = 8)
    content = models.CharField(max_length = 100)
    date = models.DateTimeField(default = datetime.datetime.now())

# class course(models.Model):
#     num = models.CharField(max_length = 8, primary_key = True)
#     student_id = models.CharField(max_length = 8)
#     course_id = models.CharField(max_length = 8)
#     teacher_id = models.CharField(max_length = 8)
#     manager_id = models.CharField(max_length = 8)

class Ex(models.Model):
    student_id = models.CharField(max_length = 8, default = '1')
    homework_num = models.CharField(max_length = 8, default = '1')
    is_view = models.BooleanField(default =False)
    is_done = models.BooleanField(default =False)
