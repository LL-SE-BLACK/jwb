# -*- coding: utf-8 -*-
__author__ = 'saltless'

from django import forms
from models import Class_info, Course_info

class CourseForm(forms.Form):
    id = forms.CharField(max_length = 8)
    name = forms.CharField(max_length = 110)
    credits = forms.FloatField()
    semester = forms.IntegerField()
    textbook = forms.CharField(max_length = 110)
    college = forms.CharField(max_length = 50)
    course_type = forms.IntegerField()

    def clean_id(self):
        addedCouseID = self.cleaned_data['id']
        if Course_info.objects.filter(id = addedCouseID):
            raise forms.ValidationError('Course number existed!')
        return addedCouseID

class CourseFormFacultyAdd(forms.Form):
    id = forms.CharField(max_length = 8)
    name = forms.CharField(max_length = 110)
    credits = forms.FloatField()
    semester = forms.IntegerField()
    textbook = forms.CharField(max_length = 110)
    course_type = forms.IntegerField()

    def clean_id(self):
        addedCouseID = self.cleaned_data['id']
        if Course_info.objects.filter(id = addedCouseID):
            raise forms.ValidationError('Course number existed!')
        return addedCouseID

class CourseFormModify(forms.Form):
    name = forms.CharField(max_length = 110)
    credits = forms.FloatField()
    semester = forms.IntegerField()
    textbook = forms.CharField(max_length = 110)
    college = forms.CharField(max_length = 50)
    course_type = forms.IntegerField()


class CourseFormFacultyModify(forms.Form):
    name = forms.CharField(max_length = 110)
    credits = forms.FloatField()
    semester = forms.IntegerField()
    textbook = forms.CharField(max_length = 110)
    course_type = forms.IntegerField()

