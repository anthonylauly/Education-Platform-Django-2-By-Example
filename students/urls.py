from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('register/',
         views.StudentRegistionView.as_view(),
         name='student_registration'),
    path('enroll-course/', 
        views.StudentEnrollCourseView.as_view(),
        name='student_enroll_course'),
    path('courses/',
        views.StudentCourseListView.as_view(),
        name='student_course_list'),
    path('course/<pk>/',
        cache_page(60*15)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail'),
    path('course/<pk>/<module id>/',
        cache_page(60*15)(views.StudentCourseDetailView.as_view()), 
        name='student_course_detail_module'),
]