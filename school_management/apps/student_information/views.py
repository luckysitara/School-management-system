from .forms import StudentForm, ClassForm, EnrollmentForm, AttendanceForm, GradeForm

# Student views
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_information/student_list.html', {'students': students})

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_information/student_form.html', {'form': form})

# Class views
def class_list(request):
    classes = Class.objects.all()
    return render(request, 'student_information/class_list.html', {'classes': classes})

def class_create(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm()
    return render(request, 'student_information/class_form.html', {'form': form})

# Enrollment views
def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'student_information/enrollment_list.html', {'enrollments': enrollments})

def enrollment_create(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()
    return render(request, 'student_information/enrollment_form.html', {'form': form})

# Attendance views
def attendance_list(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'student_information/attendance_list.html', {'attendance_records': attendance_records})

def attendance_create(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'student_information/attendance_form.html', {'form': form})

# Grade views
def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'student_information/grade_list.html', {'grades': grades})

def grade_create(request):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'student_information/grade_form.html', {'form': form})

