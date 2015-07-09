__author__ = 'Adward'
from django.conf.urls import include, url, patterns
from django.conf import settings
from django.conf.urls.static import static

from classChoose.adminer import *
from classChoose.views1 import *
from classChoose.views2 import *

urlpatterns = patterns('',
    (r'^ad1/$', admin_index),
    (r'^ad2/$', admin_page2),
    (r'^course_search/$', search),
    (r'^show_class/$', show_class),
    (r'^class_choose/$', choose_class),
    (r'^trainning_plan/$', templay),
    (r'^teacher_model/$', show_students),
    (r'^download/$', download),
    (r'^class_info/$',showCourseInfo),
    (r'^teacher_info/$',showTeacherInfo),
    url(r'^buxuan/', buXuan),
    url(r'^daohang/', daohang),

    url(r'^chooseextra/', buxuan),
    url(r'^evaluate/', pingjia1),
)