from django import forms
from .models import Curriculum, Lesson, Exam, Assessment, ReportCard

class CurriculumForm(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = ['curriculum_name', 'course_details']
        widgets = {
            'curriculum_name': forms.TextInput(attrs={'class': 'form-control'}),
            'course_details': forms.Textarea(attrs={'class': 'form-control'}),
        }

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['class_id', 'lesson_plan']
        widgets = {
            'class_id': forms.Select(attrs={'class': 'form-control'}),
            'lesson_plan': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['class_id', 'exam_schedule', 'question_paper', 'invigilation_details']
        widgets = {
            'class_id': forms.Select(attrs={'class': 'form-control'}),
            'exam_schedule': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'question_paper': forms.Textarea(attrs={'class': 'form-control'}),
            'invigilation_details': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['exam_id', 'student_id', 'marks', 'feedback']
        widgets = {
            'exam_id': forms.Select(attrs={'class': 'form-control'}),
            'student_id': forms.Select(attrs={'class': 'form-control'}),
            'marks': forms.NumberInput(attrs={'class': 'form-control'}),
            'feedback': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ReportCardForm(forms.ModelForm):
    class Meta:
        model = ReportCard
        fields = ['student_id', 'report_details']
        widgets = {
            'student_id': forms.Select(attrs={'class': 'form-control'}),
            'report_details': forms.Textarea(attrs={'class': 'form-control'}),
        }

