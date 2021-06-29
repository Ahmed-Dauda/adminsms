from django.db import models
from django import forms

# Create your models here.

class students_reg(models.Model):
    class_chice = [
        ('JSS1','JSS1'),
        ('JSS2','JSS2'),
        ('JSS3','JSS3'),
        ('SS1','SS1'),
        ('SS2','SS2'),
        ('SS3','SS3'),
        ]
    sex_chice = [
        ('male','male'),
        ('female','female'),
        ]
    status_chice = [
        ('active','active'),
        ('inactive','inactive'),
        ]
    house_choice = [
        ('red','red'),
        ('blue','blue'),
        ('yellow','yellow'),
        ('green','green'),
        ]

    names = models.CharField(
        max_length= 225, null = True, blank =True)
    dob = models.DateField(
        null = True, blank =True )
    sex = models.CharField(
        choices = sex_chice,
        max_length= 225, null = True, blank =True)
    level = models.CharField(choices = class_chice,
    max_length= 225,null = True, blank =True)
    admin_no = models.CharField(
        unique=True,
        max_length= 225, null = True, blank =True)
    house = models.CharField(
        choices= house_choice,
        max_length= 225, null = True, blank =True)
    address = models.CharField(
        max_length= 555, null = True, blank =True)
    status = models.CharField(
        choices = status_chice,
        max_length= 555, null = True, blank =True)    
    father_no = models.CharField(
        max_length= 225, null = True, blank =True)
    father_email = models.CharField(
        max_length= 225, null = True, blank =True)
    mother_no = models.CharField(
        max_length= 225, null = True, blank =True)
    mother_email = models.CharField(
        max_length= 225, null = True, blank =True)
    created_date = models.DateTimeField(
    auto_now_add = True,
    null = True, blank =True)

    def __str__(self):
        return f'{self.names}'

