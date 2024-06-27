from django import forms
from .models import Student, Class, Enrollment, Attendance, Grade

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'personal_info', 'academic_info', 'disciplinary_info']

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['class_name', 'timetable', 'room_allocation']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'class_obj', 'enrollment_date', 'withdrawal_date']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'class_obj', 'attendance_date', 'status']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'class_obj', 'grade']
