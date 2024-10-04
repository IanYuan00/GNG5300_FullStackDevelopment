from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'enrollment_date', 'grade']

        #Email validation, date form validation, and grade dropdown
        widgets = {
            'email' : forms.EmailInput(),   
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'enrollment_date': forms.DateInput(attrs={'type': 'date'}),
            'grade': forms.Select(choices=[(i, i) for i in range(1, 13)])  # Dropdown from 1 to 12
        }