from django.contrib import admin
from .models import Employee,Attendance, Leave

# Register your models here.
@admin.register(Employee)
class EmployeeDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','middle_name','last_name','username','email','phone','gender',
                        'date_of_birth','date_of_joining','nationality','village','address']

@admin.register(Attendance)
class AddAttendenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'attendance_date','in_time','out_time', 'attendance','regularization_status','description']

@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ['user', 'from_date', 'from_date_day', 'to_date', 'to_date_day', 'reason']