from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Employee(User):
    middle_name = models.CharField(max_length=150)
    phone = PhoneNumberField(null=False, blank=False,unique=True)
    gender_choices = (('M','Male'),('F','Female'))
    gender = models.CharField(max_length=1, choices=gender_choices)    
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()
    nationality = models.CharField(max_length=150)
    village = models.CharField(max_length=150)
    address = models.CharField(max_length=500)

class Attendance(models.Model):
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    attendance_date = models.DateField(default=date.today)
    in_time = models.TimeField()
    out_time = models.TimeField()
    attendance_choices = (('P','Present'),('A','Absent'))
    attendance = models.CharField(max_length=1, choices=attendance_choices)
    regularization_choices = (('A','Approved'),('D','Dismiss'))
    regularization_status = models.CharField(max_length=1, choices=regularization_choices,null=True)
    description = models.TextField(null=True)

class Leave(models.Model):
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    from_date = models.DateField()
    day_choices = (('F','Full_day'),('H','Half_day'))
    from_date_day = models.CharField(max_length=1, choices=day_choices) 
    to_date = models.DateField()
    to_date_day = models.CharField(max_length=1, choices=day_choices)
    reason = models.CharField(max_length=150)