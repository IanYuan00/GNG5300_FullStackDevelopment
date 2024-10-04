from django import forms
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'enrollment_date', 'grade']

        #Email validation, date form validation, and grade dropdown
        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),   
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'enrollment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'grade': forms.Select(choices=[(i, i) for i in range(1, 13)], attrs={'class': 'from-select'})  # Dropdown from 1 to 12
        }

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        # Add Bootstrap class to username, email, and both password fields
        self.fields['username'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Enter your username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Enter your password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Confirm your password'
        })
        self.fields['username'].help_text = ""
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user