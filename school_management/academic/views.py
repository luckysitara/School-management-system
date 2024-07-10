from django.shortcuts import render, get_object_or_404, redirect
from .forms import CurriculumForm, LessonForm, ExamForm, AssessmentForm, ReportCardForm
from .models import Curriculum, Lesson, Exam, Assessment, ReportCard

# Curriculum Views
def curriculum_list(request):
    curriculums = Curriculum.objects.all()
    return render(request, 'academic_management/curriculum_list.html', {'curriculums': curriculums})

def curriculum_create(request):
    if request.method == 'POST':
        form = CurriculumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curriculum_list')
    else:
        form = CurriculumForm()
    return render(request, 'academic_management/curriculum_form.html', {'form': form})

def curriculum_update(request, pk):
    curriculum = get_object_or_404(Curriculum, pk=pk)
    if request.method == 'POST':
        form = CurriculumForm(request.POST, instance=curriculum)
        if form.is_valid():
            form.save()
            return redirect('curriculum_list')
    else:
        form = CurriculumForm(instance=curriculum)
    return render(request, 'academic_management/curriculum_form.html', {'form': form})

def curriculum_delete(request, pk):
    curriculum = get_object_or_404(Curriculum, pk=pk)
    if request.method == 'POST':
        curriculum.delete()
        return redirect('curriculum_list')
    return render(request, 'academic_management/curriculum_confirm_delete.html', {'curriculum': curriculum})

# Lesson Views
def lesson_list(request):
    lessons = Lesson.objects.all()
    return render(request, 'academic_management/lesson_list.html', {'lessons': lessons})

def lesson_create(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
    else:
        form = LessonForm()
    return render(request, 'academic_management/lesson_form.html', {'form': form})

def lesson_update(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'academic_management/lesson_form.html', {'form': form})

def lesson_delete(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    if request.method == 'POST':
        lesson.delete()
        return redirect('lesson_list')
    return render(request, 'academic_management/lesson_confirm_delete.html', {'lesson': lesson})

# Exam Views
def exam_list(request):
    exams = Exam.objects.all()
    return render(request, 'academic_management/exam_list.html', {'exams': exams})

def exam_create(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamForm()
    return render(request, 'academic_management/exam_form.html', {'form': form})

def exam_update(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamForm(instance=exam)
    return render(request, 'academic_management/exam_form.html', {'form': form})

def exam_delete(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    if request.method == 'POST':
        exam.delete()
        return redirect('exam_list')
    return render(request, 'academic_management/exam_confirm_delete.html', {'exam': exam})

# Assessment Views
def assessment_list(request):
    assessments = Assessment.objects.all()
    return render(request, 'academic_management/assessment_list.html', {'assessments': assessments})

def assessment_create(request):
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assessment_list')
    else:
        form = AssessmentForm()
    return render(request, 'academic_management/assessment_form.html', {'form': form})

def assessment_update(request, pk):
    assessment = get_object_or_404(Assessment, pk=pk)
    if request.method == 'POST':
        form = AssessmentForm(request.POST, instance=assessment)
        if form.is_valid():
            form.save()
            return redirect('assessment_list')
    else:
        form = AssessmentForm(instance=assessment)
    return render(request, 'academic_management/assessment_form.html', {'form': form})

def assessment_delete(request, pk):
    assessment = get_object_or_404(Assessment, pk=pk)
    if request.method == 'POST':
        assessment.delete()
        return redirect('assessment_list')
    return render(request, 'academic_management/assessment_confirm_delete.html', {'assessment': assessment})

# ReportCard Views
def report_card_list(request):
    report_cards = ReportCard.objects.all()
    return render(request, 'academic_management/report_card_list.html', {'report_cards': report_cards})

def report_card_create(request):
    if request.method == 'POST':
        form = ReportCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_card_list')
    else:
        form = ReportCardForm()
    return render(request, 'academic_management/report_card_form.html', {'form': form})

def report_card_update(request, pk):
    report_card = get_object_or_404(ReportCard, pk=pk)
    if request.method == 'POST':
        form = ReportCardForm(request.POST, instance=report_card)
        if form.is_valid():
            form.save()
            return redirect('report_card_list')
    else:
        form = ReportCardForm(instance=report_card)
    return render(request, 'academic_management/report_card_form.html', {'form': form})

def report_card_delete(request, pk):
    report_card = get_object_or_404(ReportCard, pk=pk)
    if request.method == 'POST':
        report_card.delete()
        return redirect('report_card_list')
    return render(request, 'academic_management/report_card_confirm_delete.html', {'report_card': report_card})

