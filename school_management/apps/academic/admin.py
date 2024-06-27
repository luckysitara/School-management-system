from django.contrib import admin
from .models import Curriculum, Lesson, Exam, Assessment, ReportCard

admin.site.register(Curriculum)
admin.site.register(Lesson)
admin.site.register(Exam)
admin.site.register(Assessment)
admin.site.register(ReportCard)
