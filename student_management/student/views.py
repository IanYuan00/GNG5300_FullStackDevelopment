from django.shortcuts import render, redirect, get_object_or_404
from student.models import Student
from student.forms import StudentForm

# Create your views here.
#DIsplay a list of all students
def student_index(request):
    students = Student.objects.all().order_by('last_name')
    return render(request, 'student/index.html', {'students': students})

#Display the details of a single student
def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student/detail.html', {'student': student})

#Add a new student
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_index')
    else:
        form = StudentForm()
        
    return render(request, 'student/add.html', {'form': form})

#Edit an existing student
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=pk)
    else:
        form = StudentForm(instance = student)

    return render(request, 'student/edit.html', {'form': form, 'student': student})