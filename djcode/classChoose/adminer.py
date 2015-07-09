# -*- coding: utf-8 -*-
from django.contrib.auth.models import *
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from  datetime  import  *
import time
from django.http import HttpResponseRedirect
from classChoose.login import *

from django.contrib import admin
from django.db.models import Q
from django.db.models import query
from django.template.loader import get_template
from django.template import RequestContext, Context
from django.contrib.auth.models import User
from classChoose.models import *
from django.http import HttpResponse,HttpRequest
from django.shortcuts import render
import random
from django.template import loader
from.models import *
import json
import datetime
#from datetime import datetime
import time
import threading
# Register your models here.

#@login_required(login_url="/login/")  
def  add_done(class_ID,student_ID):
    #forcelogout(request)
    #提取得到教学班id
    print ("in adding")
    flag=""
    #class_ID = request.POST.get('class_id_hidden')
    #student_ID = request.POST.get('add_id')
    qset = (Q(Class__id = class_ID)&Q(student__id = student_ID))
    n = Class_table.objects.filter(qset).count()
    if n==0:
        add_info = Class_table()
        Class = Class_info.objects.get(id=class_ID)
        print(Class)
        student = Student_user.objects.get(id=student_ID)
        print(student)
        #add_info.id = '%d' %(random.randint(1, 100))
        add_info.id = class_ID+student_ID
        add_info.Class = Class     #query Class_info by class_id
        add_info.student = student     #query Student_user by student_id
        add_info.status = 1
        print (add_info)
        flag = add_info.save()
        print(flag)
        return (flag)
    else:
        choose_info=Class_table.objects.get(qset)
        choose_info.status=1
        choose_info.save()
        return (flag)


#@login_required
def  delete_done(class_ID,students_ID_list):
    #forcelogout(request)
    print ("in deleting")
    flag=True
    #class_ID = request.POST.get('class_id_for_del')
    #students_ID_list = list()
    #student_ID_list = (request.POST.get('hiddenInput')).split('A')
    #print (class_ID)
    #print (student_ID_list[0])
    #提取class_id和student_id(已经选中)
    #delete_info = Class_table.objects.filter(class_id=class_ID,student_id=student_ID)
    print (len(students_ID_list))
    for i in range(0,len(students_ID_list)-1):
        qset = (Q(Class__id=class_ID)&Q(student__id=students_ID_list[i]))
        delete_info = Class_table.objects.get(qset)
        delete_info.delete()
    if i==len(students_ID_list)-1:
        return (1)
    else:
        return (0)
    #if flag == 1:
    #return HttpResponse('delete success!')
    #else:
    #return HttpResponse('delete error!')



#@login_required
def select_students_list(class_ID):
    #forcelogout(request)
    #print (class_ID)
    #print (Class_table.objects.all())
    qset = (Q(Class__id = class_ID)&Q(status = 1))
    choose_list = Class_table.objects.filter(qset).order_by('student__id') #Class_table和Student_user的交集
    #print (choose_list)
    students_id_list = list()
    students_list = list()
    #print (Student_user.objects.all())
    #print (choose_list[0].student.id)
    #print (choose_list.count())
    for choose in choose_list:
        #print ("a")
        #print (choose_list[i].student.id)
        students_id_list.append(choose.student.id)
        students_list.append(Student_user.objects.get(id=choose.student.id))
    return (students_list,students_id_list)

#@login_required
def sift(Time,classes_list,admin_college):
    #forcelogout(request)
    #time = request.GET['sift_time']
    print("in sifting")
    while 1:
        if  (datetime.datetime.now())>=Time:
            print("It's time now")
            print (Class_table.objects.all())
            #print("classes_list:")
            #print (classes_list)
            for Class in classes_list: #for every class
                number = (Class_info.objects.get(id=Class.id)).capacity
                qset = (Q(Class__id = Class.id)&Q(status = 0))
                choose_list = Class_table.objects.filter(qset)
                if(len(choose_list)==0):  #if no students choose
                    break
                else:
                    print("Class:")
                    print(Class)
                    print("number:")
                    print(number)
                    #print("choose_list:")
                    print(choose_list)
                    print(len(choose_list)-1)
                    if len(choose_list)<=number:     #if choose students less than capacity
                        print ("in choose students less than capacity")
                        for Choose in choose_list:
                            Choose.status=True
                            Choose.save()
                    else:           #students more than capacity,we use score  to select
                        score_list = list()
                        print (choose_list)
                        for i in range(0,len(choose_list)):
                            print ("in for")
                            if choose_list[i].student.college==admin_college: #the same college as admin plus 1
                                score=2
                                if choose_list[i].student.grade==4:        #the last year students plus 1
                                    score = score+1
                                else:
                                    score = score+0
                            else:
                                score=0
                                if choose_list[i].student.grade==4:        #the last year students plus 1
                                    score = score+1
                                else:
                                    score = score+0
                            print("score")
                            print(score)
                            score_list.append(score)
                        #print(score_list)
                        for j in range(0,number): #choose the top number scored students
                            print("in choose for")
                            Max = score_list[0]
                            for Score in score_list:
                                if Score > Max:
                                    Max=Score
                            #print("Max:")
                            #print (Max)
                            index=score_list.index(Max)
                            top_choose = choose_list[index]
                            print("status:")
                            print (top_choose.status)
                            top_choose.status=True
                            top_choose.save()
                            print("status again:")
                            print (top_choose.status)
                            score_list[index]=0  #except the choosen top ones
                        for Choose in choose_list:   #delete other students' records
                            if Choose.status!=True:
                                Choose.delete()
                        print("sifting finishing")
            break
        #siftee = random.sample(Class,(Class.count()-number))
        #siftee.delete()
        else:
            print("It's not time")
            time.sleep(60)
            continue



#@login_required
def  admin_index(request):
    #forcelogout(request)
    try:
        admin_id = request.GET['id']

        if admin_id=="2":
            print ("if")
            return HttpResponse("permission denied!")

        print ("id:"+admin_id)
        admin = Admin_user.objects.get(id=admin_id)#the currently loggedin user
        a=False
        if a:
            #if admin.is_authenticated() == False:
            return render(
                request,
                "login.html"
            )
        else:
            admin_college = admin.college
            #Course_info = Course_info.objects.filter(college=admin_college)
            classes_list = Class_info.objects.filter(course__college=admin_college).order_by('-course__id')#本学院的所有课
            #sorted(classes_list)
            #for every class in classes_list
            #class.remian=class.capacity-(Class_table.objects.filter(id=class.id).count())
            #print(classes_list)
            for Class in classes_list:
                qset = (Q(Class__id = Class.id)&Q(status = 1))
                Class.remain = Class.capacity - (Class_table.objects.filter(qset).count())
            #print (classes_list)
            if request.method=='GET':
                return render(
                    request,
                    "adminpage1.html",
                    {'classes':classes_list, 'admin':admin},
                )

            else:
                ch_time=choose_time(id="1",	start_time =request.POST.get('start_time') ,end_time =request.POST.get('sift_time') ,buXuan_start_time =request.POST.get('buxuan_time') ,buXuan_end_time = request.POST.get('end_buxuan_time'))
                ch_time.save()
                print (choose_time.objects.all())
                Time = request.POST.get('sift_time')
                time.end_time = Time
                print (Time)
                Time_=datetime.datetime.now()
                Time_= datetime.datetime.strptime(Time,"%Y-%m-%d %H:%M:%S")
                #time = datetime.datetime.strptime(Time,"%Y-%m-%d %H:%M:%S").datetime()
                print(Time_)
                thread1=threading.Thread(target=sift,name="sifter",args=(Time_,classes_list,admin_college))
                thread1.start()
                return render(
                    request,
                    "adminpage1.html",
                    {'classes':classes_list, 'admin':admin},
                )
    except:
        return HttpResponse("permission denied!")


#@login_required
def  admin_page2(request):
    try:
        #forcelogout(request)
        class_ID = request.GET.get('class_id')
        #print (students_list)
        #print (students_id_list)
        if request.method == 'GET':
            #class_ID = request.GET.get('class_id')
            print (class_ID)
            a=""
            (students_list,students_id_list) = select_students_list(class_ID)
            return render(
                request,
                "adminpage2.html",
                {'students':students_list,'List':students_id_list,'flag':a}
            )
        else :
            print ("in POST")
            #class_ID = request.POST.get('class_id_for_del')
            #students_ID_list = list()
            #student_ID_list = (request.POST.get('hiddenInput')).split('A')
            #print (class_ID)
            #print (student_ID_list)
            Tag = request.POST.get('tag')
            print (Tag)
            if Tag == "1":
                print ("haha")
                #class_ID = request.POST.get('class_id_hidden')
                student_ID = request.POST.get('add_id')
                print (student_ID)
                #add_done(Request)
                flag=add_done(class_ID,student_ID)
                (students_list,students_id_list) = select_students_list(class_ID)
                return render(
                    request,
                    "adminpage2.html",
                    {'students':students_list,'List':students_id_list,'flag2':flag}
                )
            else:
                student_IDs = request.POST.get('hiddenInput')
                students_ID_list=list()
                if(student_IDs):
                    students_ID_list = student_IDs.split('A')
                print ("class_ID:"+class_ID)
                print (students_ID_list)
                flag=delete_done(class_ID,students_ID_list)
                (students_list,students_id_list) = select_students_list(class_ID)
                return render(
                    request,
                    "adminpage2.html",
                    {'students':students_list,'List':students_id_list,'flag':flag}
                )
    except:
        return HttpResponse("permission denied!")



#@login_required
def buXuan(request):
    try:
        #forcelogout(request)
        print ("buXuan")
        class_ID = request.GET.get('class_id')
        Class=Class_info.objects.get(id=class_ID)
        cid=class_ID
        cname =Class.course.name

        print (class_ID)
        #class_ID = request.GET.get('class_id')
        #print (students_list)
        #print (students_id_list)
        if request.method == 'GET':
            #class_ID = request.GET.get('class_id')
            print (class_ID)
            a=""
            buXuan_list = buXuan_info.objects.filter(Class__id = class_ID).order_by('student__id')
            print (buXuan_info.objects.all())
            #(students_list,students_id_list) = select_students_list(class_ID)
            students_id_list=list()
            for buXuan in buXuan_list:
                students_id_list.append(buXuan.student.id)

            return render(
                request,
                "bySelect.html",
                {'buXuan':buXuan_list,'List':students_id_list,'cid':cid,'cname':cname}
            )
        else :                                          #补选添加
            print ("in POST")
            #class_ID = request.POST.get('class_id_for_del')
            #students_ID_list = list()
            #student_ID_list = (request.POST.get('hiddenInput')).split('A')
            #print (class_ID)
            #print (student_ID_list)

            print ("haha")
            #class_ID = request.POST.get('class_id_hidden')
            student_ID = request.POST.get('add_id')[:-1]
            print ("student_ID:")
            print (student_ID)
            #add_done(Request)
            flag=add_done(class_ID,student_ID)
            print ("flag:")
            print (flag)


            qset = (Q(Class__id = class_ID)&Q(student__id = student_ID))
            buXuan1=buXuan_info.objects.get(qset)
            buXuan1.delete()
            #(students_list,students_id_list) = select_students_list(class_ID)
            buXuan_list = buXuan_info.objects.filter(Class__id = class_ID).order_by('student__id')
            students_id_list=list()
            for buXuan in buXuan_list:
                students_id_list.append(buXuan.student.id)

            return render(
                request,
                "bySelect.html",
                {'buXuan':buXuan_list,'List':students_id_list,'cid':cid,'cname':cname}
            )
    except:
        return HttpResponse("permission denied!")