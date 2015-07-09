from django.contrib import admin
from IMS.models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'credits', 'semester', 'textbook', 'college', 'course_type')
    search_fields = ('id', 'name')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact', 'name', 'gender', 'college', 'major', 'grade', 'gpa', 'credits', 'isSpecial')
    search_fields = ('id', 'name', 'college')

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact', 'name', 'gender', 'college', 'major', 'degree', 'title', 'isSpecial')
    search_fields = ('id', 'name', 'college')

class AdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact', 'name', 'gender', 'college')
    search_fields = ('id', )

admin.site.register(Student_user, StudentAdmin)
admin.site.register(Faculty_user, FacultyAdmin)
admin.site.register(Admin_user, AdminAdmin)
admin.site.register(Course_info, CourseAdmin)
admin.site.register(Class_info)
admin.site.register(Class_table)
