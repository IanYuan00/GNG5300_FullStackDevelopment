from django.shortcuts import render, redirect, get_object_or_404
from student.models import Student
from student.forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
#DIsplay a list of all students
def student_index(request):
    students = Student.objects.all().order_by('last_name')

    # Set up pagination with 10 students per page
    paginator = Paginator(students, 10)  # Show 10 students per page
    
    # Get the page number from the request (defaults to 1)
    page_number = request.GET.get('page')
    
    # Get the students for the requested page
    students = paginator.get_page(page_number)

    return render(request, 'student/index.html', {'students': students})

#Display the details of a single student
def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student/detail.html', {'student': student})

#Add a new student
@login_required
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
@login_required
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

#Delete a student information
@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_index')
    return render(request, 'student/delete.html', {'student': student})

def student_search(request):
    query = request.GET.get('q')  #Get the search query from the request
    students = None
    if query:
        students = Student.objects.filter(first_name__icontains=query) | Student.objects.filter(last_name__icontains=query)
    return render(request, 'student/search.html', {'students': students, 'query': query})
