
from clasChoose.models import *

admin1 = Admin_users(id="1",contact="123",name="zch",college="计算机科学与技术学院")
admin1.save()

student1 = Student_user(id="1",contact="123456",name="小明",gender=0,college="计算机科学与技术学院",major="计算机",grade=4,gpa=4.5,credits=99.5,isSpecial=0)
student1.save()
#student2 = Student_user(id="2",contact="123456",name="XiaoHong",gender=1,college="123",major="jisuanji",grade=2,gpa=4.7,credits=100.5)
#student2.save()
#student3 = Student_user(id="3",contact="123456",name="XiaoLi",gender=1,college="1234",major="xindian",grade=4,gpa=4.8,credits=110.5)
#student3.save()

course1 = Course_info(id="1",name="数据挖掘",college="计算机科学与技术学院",credits=2.0,semester=1,textbook= 'Data mining',course_type=1,introduce = "呵呵")
course1.save()
#course2 = Course_info(id="2",name="SE",college="123",credits=2.0,semester=2,textbook= 'Software engineering',style=1)
#course2.save()
#course3 = Course_info(id="3",name="QiPa",college="123",credits=4.0,semester=1,textbook= 'QiPa',style=2)
#course3.save()

teacher1 = Faculty_users(id="1",contact="123456",name="蔡登",college="计算机科学与技术学院",major="计算机",degree="doctor",title="professor")
teacher1.save()
#teacher2 = Faculty_users(id="2",contact="123456",name="ChenYue",college="123",major="jisuanji",degree="doctor",title="professor")
#teacher2.save()

class1 = Class_info(id="1",course=course1,teacher=teacher1,time="3012",room="101",examdate="20150607",examtime="12:21",examroom="101",capacity=60,remain=60,semester=12,year="2014-2015",language="English")
class1.save()
#class2 = Class_info(id="2",course=course1,teacher=teacher2,time="2013",room="102",examdate="20150607",examtime="12:21",examroom="102",capacity=60,remain=60,semester=12,year="2014-2015",method="English")
#class2.save()
#class3 = Class_info(id="3",course=course2,teacher=teacher2,time="4012|2012",room="103",examdate="20150608",examtime="16:21",examroom="103",capacity=30,remain=30,semester=34,year="2013-2014",method="English")
#class3.save()
#class4 = Class_info(id="4",course=course3,teacher=teacher2,time="4012",room="201",examdate="20151008",examtime="10:30",examroom="201",capacity=2,remain=2,semester=34,year="2013-2014",method="English")
#class4.save()

#class_choose1 = Class_table(id="1",student=student1,Class=class1,status=0)
#class_choose1.save()
#class_choose2 = Class_table(id="2",student=student2,Class=class2,status=1)
#class_choose2.save()
#class_choose3 = Class_table(id="3",student=student1,Class=class2,status=1)
#class_choose3.save()
#class_choose4 = Class_table(id="4",student=student2,Class=class1,status=1)
#class_choose4.save()
#class_choose5 = Class_table(id="5",student=student2,Class=class3,status=0)
#class_choose5.save()
#class_choose6 = Class_table(id="180",student=student3,Class=class3,status=0)
#class_choose6.save()
class_choose1 = Class_table(id="11",student=student1,Class=class1,status=0)
class_choose1.save()
#class_choose2 = Class_table(id="24",student=student2,Class=class4,status=0)
#class_choose2.save()
#class_choose3 = Class_table(id="34",student=student3,Class=class4,status=0)
#class_choose3.save()

college_demand1 =  college_demand(id="1",college="计算机科学与技术学院",	majorCourse_demand =20 ,optionCourse_demand =20 ,generalCourse_demand = 20)
college_demand1.save()

#buXuan_info1= buXuan_info(id="1",student =student1 ,Class =class1 ,reason ="大四狗")
#buXuan_info1.save()

#user = User.objects.create_user(username='1',password='1',first_name = "0")
#user.save
#user = User.objects.create_user(username='2',password='2',first_name = "1")
#user.save
#user = User.objects.create_user(username='3',password='3',first_name = "2")
#user.save

count1=count(id="1",value=0)
count1.save()