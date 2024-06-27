from django.db import models

class Curriculum(models.Model):
    curriculum_name = models.CharField(max_length=100)
    course_details = models.JSONField()

class Lesson(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    lesson_plan = models.JSONField()

class Exam(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    exam_schedule = models.DateField()
    question_paper = models.JSONField()
    invigilation_details = models.JSONField()

class Assessment(models.Model):
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = models.IntegerField()
    feedback = models.TextField()

class ReportCard(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    report_details = models.JSONField()

