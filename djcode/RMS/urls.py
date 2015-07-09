from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^Resource.html',views.resource,name='resource'),
	url(r'^ResourceCourse.html',views.resourcecourse,name='resourcecourse'),
	url(r'^ResourceList.html',views.resourcelist,name='resourcelist'),
	url(r'^Notice.html',views.notice_display,name='notice_display'),
	url(r'^NoticeList.html',views.noticelist,name='noticelist'),
	url(r'^HomeworkList.html',views.homeworklist,name='homeworklist'),
	url(r'^Homework.html',views.homework_display,name='homework_display'),
	url(r'^DownloadHomework.html',views.gethomework_list,name='gethomework_list'),
	url(r'^AssignNotice.html',views.assignnotice,name='assignnotice'),
	url(r'^AssignHomework.html',views.assignhomework,name='assignhomework'),
	url(r'^Assign_Notice',views.notice_assign,name='notice_assign'),
	url(r'^Resource_Upload',views.resource_upload,name='resource_upload'),
	url(r'^file_download',views.file_download,name='sb'),
	url(r'^delete_resource',views.delete_resource,name='Delete_Resource'),
	url(r'^stick_resource',views.stick_resource,name='Stick_resource'),
	url(r'^cancal_stick_resource',views.cancal_stick_resource,name='Cancal_stick_resource'),
	url(r'^search_resource',views.search_resource,name='search_resource'),
	url(r'^delete_notice',views.delete_notice,name='delete_notice'),
	url(r'^homework_upload',views.homework_upload,name='homework_upload'),
	url(r'^delete_homework',views.delete_homework,name='delete_homework'),
	url(r'^homework_assign',views.homework_assign,name='homework_assign'),
]