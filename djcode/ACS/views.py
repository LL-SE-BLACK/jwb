# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from form import sourse_form
from django.contrib import staticfiles
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext 
from django.views.decorators.csrf import csrf_exempt
from models import Application as apply
from models import classroom
from IMS.models import Course_info, Class_info, Faculty_user
from django.contrib.auth.models import User
from django.contrib import auth
from AutoCourseArrangement import AutoCourseArrange
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
import json

@csrf_exempt
def Logout(request):
	auth.logout(request)
	return HttpResponseRedirect('..')

@csrf_exempt
def TeachingResourse(request, offset):#管理教室
	if not auth_admin(request):
		return HttpResponseRedirect('../mca')#非法url
	
	del_r = ''
	add_r = ''
	mod_r = ''
	
	admin = auth_admin(request)
	if request.method == 'POST':
		f = request.POST
	else:
		f = 0
	if f:
		if offset == "add" :#插入
			
			try:
				try:
					p = classroom.objects.create( name = f["cr_Name"], type = f["cr_Type"], capacity = f["cr_capa"], campus = f["cr_camp"])
				except StandardError, e:
					print e
				p.save()
				add_r = 'add success'
			except StandardError, e:
				add_r = 'add fail'
		elif offset == "del" :#删除
			try:
				p = classroom.objects.get(id = f["cr_ID"])
				p.delete()
				del_r = 'delete success'
			except StandardError, e:
				del_r = 'delete fail'
		elif offset == "mod":#更新
			try:
				p = classroom.objects.filter(id = f["cr_ID"])
				p.update(capacity = f["cr_capa"])
				mod_r = 'modify success'
			except StandardError, e:
				mod_r = 'modify fail'
		else:
			return HttpResponse("error")#其他
	return render_to_response('cr.html', {'admin': admin, 'add_result':add_r, 'del_result':del_r, 'mod_result':mod_r})

@csrf_exempt
def CourseArrange(request, offset):
	if not auth_admin(request):
		return render_to_response('mca.html')
	res = ''
	admin = auth_admin(request)
	if offset == 'automatic':#按下按钮开始调课
		res = 'Done'
		auto = AutoCourseArrange()
		auto.run()
		auto.Save_Current_Schedule()
		print "Done"
	return render_to_response('acs.html', {'sch_result':res, 'admin':admin})

@csrf_exempt
def CourseApply(request, offset):
	del_r = ''
	add_r = ''
	
	admin = auth_admin(request)
	try:
		ApplyList = apply.objects.filter(teacherID=request.user.username)#获得教师的课程表信息
		print ApplyList
	except StandardError, e:
		f = 0;
	for i in ApplyList:
		i.classTime = timeadj(i.classTime, "application")#解码
		
	if request.method == 'POST':
		f = request.POST
	else:
		f = 0
	if f:
		if offset == "add_cl" :#插入
			w1 = f["cl_Time1"]
			t1 = f["cl_Hour1"]
			w2 = f["cl_Time2"]
			t2 = f["cl_Hour2"]
			r = ''
			#处理时间
			flag = 1
			t1 = dec_time(int(t1))

			r = []
			for i in t1:
				r.append([int(w1), i])
			if t2 != None and t2:
				flag = 2
				t2 = dec_time(int(t2))
				for i in t2:
					r.append([int(w2), i])
			t = json.dumps(r)
			try:
				p = apply.objects.create(
										id = f["cl_ID"], 
										cuz_ID = f["cuz_ID"],
										classHour = flag,
										teacherID = request.user.username,
										classTime = t,
										campus = f["cl_Camp"], 
										class_capacity = f["cl_Capa"])
				
				p.save()
				add_r = 'add seccess'
			except StandardError, e:
				add_r = 'add fail'
	
		else:	#删除
			try:
				p = apply.objects.get(id = f["cl_ID"])
				p.delete()
				del_r = 'delete seccess'
			except StandardError, e:
				del_r = 'delete fail'
	return render_to_response('mca.html', {'admin': admin, 'add_result':add_r, 'del_result':del_r, 'applylist':ApplyList})

@csrf_exempt
def Index(request):#登录部分
	if request.user.is_anonymous():
		u = '/'
		return HttpResponseRedirect(u)
	username = request.user.username
	groups = request.user.groups.values_list('name', flat=True)
	if len(groups) > 0:
		Type = groups[0]
	else:
		Type = 'admin'
	#assert False
	if Type == 'teacher':
		u = '/ACS/mca/'
		return HttpResponseRedirect(u)
	elif  Type == 'admin':
		u = '/ACS/cr/'
		return HttpResponseRedirect(u)
	else:
		u = '/'
		return HttpResponseRedirect(u)
	
	
@csrf_exempt
def CourseSearch(request):#课程查询
	try:
		CourseList = Class_info.objects.filter(teacher=request.user.username)
		CourseTable = ListToTable(CourseList)
	except StandardError, e:
		CourseTable = ""
		print e
	return render_to_response('tcs.html', {'schedule':CourseTable, 'admin':request.user.is_staff})

@csrf_exempt
def ClassroomInquiry(request):
	if request.method == 'POST':
		try:
			print "classroom:", request.POST["classroom_id"]
			try:
				CourseList = Class_info.objects.filter(room = request.POST["classroom_id"])
			except StandardError, e:
				print e
			try:
				for i in CourseList:
					i.time = timeadj(i.time, "class_info")
					print i.time
			except StandardError, e:
				print e
		except StandardError, e:
			print e
			CourseList = None
	else:
		CourseList = None
	#assert False
	return render_to_response('ci.html', {'roomschedule':CourseList, 'admin':auth_admin(request)})

@csrf_exempt
def CourseOperation(request, offset):
	if not auth_admin(request):
		return HttpResponseRedirect('../mca')
	del_r = ''
	add_r = ''
	del_2 = ''
	add_2 = True
	admin = auth_admin(request)
	if request.method == 'POST':
		f = request.POST
	else:
		f = 0
	
	if offset == 'add_cz':#增加课程
		try:
			p = Course_info.objects.create(id = f["cz_ID"], 
										name = f["cz_Name"], 
										credits = f["cz_Credits"], 
										semester = f["cz_Term"],
										textbook = f["cz_Testbook"],
										college = f["cz_College"],
										#time = f["cz_Time"], 
										)
			p.save()
			add_r = 'add seccess'
		except StandardError, e:
				add_r = 'add fail'
	elif offset == 'del_cz':
		try:
			p = Course_info.objects.get(id = f["cz_ID"])
			p.delete()
			del_r = 'delete seccess'
		except StandardError, e:
			del_r = 'delete fail'
	elif offset == 'add_cl':#增加教学班
		w1 = f["cl_Time1"]
		t1 = f["cl_Hour1"]
		w2 = f["cl_Time2"]
		t2 = f["cl_Hour2"]
		#时间处理
		t1 = dec_time(int(t1))
		
		r = []
		for i in t1:
			r.append([int(w1), i])
		if t2 != None and t2:
			t2 = dec_time(int(t2))
			for i in t2:
				r.append([int(w2), i])
		t = json.dumps(r)
		#search whether there is a conflict
		teachertime = 0
		roomtime = 0
		over= 0
		#检查同一老师同一时间
		a = Class_info.objects.filter(teacher = f["teac_ID"], time = t)#
		teachertime = a and 1 or 0
		print "same teacher same time", a
		#检查相同教室相同时间
		a = Class_info.objects.filter(room = f["cl_room"], time = t)
		roomtime = a and 1 or 0
		a = classroom.objects.filter(name = f["cl_room"])
		print "same classroom same time", a
		#over = a[0].capacity
		#检查容量
		if (not a) or (a[0].capacity < int(f["cl_Capa"])) or (int(f["cl_Capa"]) < 0):
			add_2 = False
			print not a
			print a[0].capacity < int(f["cl_Capa"])
			print int(f["cl_Capa"]) < 0
			print "capacity"
		elif 	(teachertime  + roomtime  >= 1):
			add_2 = False
			print "either"
		else:
			try:
				p = Class_info.objects.create(
											id = f["cl_ID"],
											course = Course_info.objects.get(id = f["cuz_ID"]), 
											teacher = Faculty_user.objects.get(id = f["teac_ID"]),
											time = t,
											room = f["cl_room"], 
											capacity = int(f["cl_Capa"])
											)
				p.save()
				add_2 = True			
			except StandardError, e:
				add_2 = False
				print e
	elif offset == 'del_cl':
		try:
			p = Class_info.objects.get(id = f["cl_ID"])
			p.delete()
			del_2 = 'delete seccess'
		except StandardError, e:
			del_2 = 'delete fail'
	print(add_2)
	return render_to_response('cp.html', {'admin': admin, 'add1_result':add_r, 'del1_result':del_r, 'add2_result':add_2, 'del2_result':del_2,})

def dec_time(t):#课程时间
	if t == 1:
		return [1,2]
	elif  t == 2:
		return  [3,4]
	elif  t == 3:
		return  [3,4,5]
	elif  t == 4:
		return  [6,7,8]
	elif  t == 5:
		return  [7,8]
	elif  t == 6:
		return  [9,10]
	elif  t == 7:
		return  [11,12]
	elif  t == 8:
		return  [11,12,13]
	else:
		return None

def timeadj(t, mode):
	#t = json.loads(t)
	if mode=="application":
		t = json.loads(t)
	else:
		t = TurnGroupThreeToUs(t)
	tmp = ""
	for i in t:
		if i[0] == 1:
			i[0] = 'Mon'
		elif i[0] == 2:
			i[0]  = 'Tue'
		elif i[0] == 3:
			i[0] = 'Wed'
		elif i[0] == 4:
			i[0] = 'Thu'
		elif i[0] == 5:
			i[0] = 'Fri'
		elif i[0] == 6:
			i[0] = 'Sat'
		elif i[0] == 7:
			i[0] = 'Sun'
		else:
			return None
		tmp = tmp + i[0] + str(i[1]) + " "
	return tmp

def ListToTable(CourseList):
	table = []
	for i in range(0, 5):
		row = []
		for j in range(0, 7):
			row.append(False)
		table.append(row)
	ckt = [0,0,1,1,1,2,2,2,3,3,4,4,4]
	for course in CourseList:
		print(course.course.name)
		print(course.room)
		#t = json.loads(course.time)
		t = TurnGroupThreeToUs(course.time)
		#print(t)
		for ct in t:
			#print(ct)
			table[ckt[ct[1] - 1]][ct[0] - 1] = course
	#print(table)
	print table
	return table

@login_required
def auth_admin(request):
	username = request.user.username
	groups = request.user.groups.values_list('name', flat=True)
	if len(groups) > 0:
		Type = groups[0]
	else:
		Type = 'admin'
	if Type == 'admin':
		return True
	else:
		return False

def TurnGroupThreeToUs(time):
	ret = []
	for i in time.split("|"):
		for j in i[2:]:
			ret.append([int(i[0]), int(j)])
	print ret
	return ret