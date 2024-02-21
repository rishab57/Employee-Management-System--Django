from django import forms
from .models import Employee

class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'dept', 'salary', 'bonus', 'role', 'phone', 'doj']