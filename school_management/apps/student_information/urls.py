from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('students/new/', views.student_create, name='student_create'),
    
    path('classes/', views.class_list, name='class_list'),
    path('classes/new/', views.class_create, name='class_create'),
    
    path('enrollments/', views.enrollment_list, name='enrollment_list'),
    path('enrollments/new/', views.enrollment_create, name='enrollment_create'),
    
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/new/', views.attendance_create, name='attendance_create'),
    
    path('grades/', views.grade_list, name='grade_list'),
    path('grades/new/', views.grade_create, name='grade_create'),
]

