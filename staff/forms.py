from .models import Institutions
from django import forms
from django.contrib.auth.models import User
from staff.models import Staff
from students.models import Student
from tkinter import Widget
from django.forms import widgets


class StaffEditForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('__all__')
        # exclude= ['institute_status','user']
        
        
class EnrollStudentsForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['allowregistration',]
        # exclude= ['institute_status','user']
        

class StudentEditForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ['studentuser','staffuser']
