from django import forms
from .models import Employee

class StudentForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

class TeacherForm(forms.Form):
    firstname=forms.CharField(label="Enter First Name:",max_length=100)
    lastname=forms.CharField(label="Enter Last Name:",max_length=100)
    email=forms.EmailField(label="Enter valid Email:")
    file=forms.FileField(label="Enter Your Document:")
