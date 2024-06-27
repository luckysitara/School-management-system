from django.urls import path
from . import views

urlpatterns = [
    path('curriculums/', views.curriculum_list, name='curriculum_list'),
    path('curriculums/new/', views.curriculum_create, name='curriculum_create'),
    path('curriculums/<int:pk>/edit/', views.curriculum_update, name='curriculum_update'),
    path('curriculums/<int:pk>/delete/', views.curriculum_delete, name='curriculum_delete'),
    
    path('lessons/', views.lesson_list, name='lesson_list'),
    path('lessons/new/', views.lesson_create, name='lesson_create'),
    path('lessons/<int:pk>/edit/', views.lesson_update, name='lesson_update'),
    path('lessons/<int:pk>/delete/', views.lesson_delete, name='lesson_delete'),

    path('exams/', views.exam_list, name='exam_list'),
    path('exams/new/', views.exam_create, name='exam_create'),
    path('exams/<int:pk>/edit/', views.exam_update, name='exam_update'),
    path('exams/<int:pk>/delete/', views.exam_delete, name='exam_delete'),

    path('assessments/', views.assessment_list, name='assessment_list'),
    path('assessments/new/', views.assessment_create, name='assessment_create'),
    path('assessments/<int:pk>/edit/', views.assessment_update, name='assessment_update'),
    path('assessments/<int:pk>/delete/', views.assessment_delete, name='assessment_delete'),

    path('report_cards/', views.report_card_list, name='report_card_list'),
    path('report_cards/new/', views.report_card_create, name='report_card_create'),
    path('report_cards/<int:pk>/edit/', views.report_card_update, name='report_card_update'),
    path('report_cards/<int:pk>/delete/', views.report_card_delete, name='report_card_delete'),
]

