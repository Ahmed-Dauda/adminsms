from studentsms.models import students_reg 
from django import forms
from django.forms import ModelForm
from django.db import models

class studentsform(forms.ModelForm):
    class Meta:
        model= students_reg
        fields= '__all__'
        # widgets ={
        #     'names':forms.TextInput(attrs={'class':'input'})
        # }