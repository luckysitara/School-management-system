from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    personal_info = models.JSONField()
    academic_info = models.JSONField()
    disciplinary_info = models.JSONField()

    def __str__(self):
        return f"{self.user.username}"

class Class(models.Model):
    class_name = models.CharField(max_length=50)
    timetable = models.JSONField()
    room_allocation = models.JSONField()

    def __str__(self):
        return self.class_name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    withdrawal_date = models.DateField(null=True, blank=True)

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    grade = models.CharField(max_length=5)
