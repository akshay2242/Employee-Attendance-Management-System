from django.http import request
from django.shortcuts import render,HttpResponseRedirect
from .models import Attendance, Employee, Leave
from django.contrib.auth import authenticate, login, logout
from .forms import AddEmployessForm,AddAttendanceForm, LeaveForm,LoginForm,Emp_AddAttendanceForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
# Home 
def home(request):
    return render(request, 'home.html')

# Employee Login
def employee_login(request):
    global uname
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:    
                    login(request,user)
                    return HttpResponseRedirect('/employee_dashboard/')

        else:        
            form = LoginForm()
        return render(request, 'employee_login.html', {'form':form})
    else:
        return HttpResponseRedirect('/employee_dashboard/')

# Employee Dashboard
@login_required
def employee_dashboard(request):
    c_user = request.user
    return render(request, 'employee_dashboard.html', {'c_user':c_user})

# Employee Add Attendance
@login_required
def emp_add_attendance(request):
    c_user = request.user
    if request.method == "POST":
        form = Emp_AddAttendanceForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            form = Emp_AddAttendanceForm()     
            
    else:
        form = Emp_AddAttendanceForm()
    return render(request, 'emp_add_attendance.html', {'form':form, 'c_user':c_user})

# Employee attendance Details
@login_required
def employee_attendance_details(request):
    data = Attendance.objects.filter(user=request.user)
    return render(request, 'emp_attendance_details.html', {'data':data})

# Apply For Leaves
@login_required
def leave_view(request):
    if request.method == "POST":
        form = LeaveForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()    
            form = LeaveForm()     
            
    else:
        form = LeaveForm()
    return render(request, 'employee_leave.html', {'form':form})

# Admin Login
def admin_login(request):
    global uname
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:    
                    login(request,user)
                    return HttpResponseRedirect('/admin_dashboard/')

        else:        
            form = LoginForm()
        return render(request, 'admin_login.html', {'form':form})
    else:
        return HttpResponseRedirect('/admin_dashboard/')

# Admin Dashboard
@staff_member_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

# Add Employee
@staff_member_required
def add_employee(request):
    if request.method == "POST":
        form = AddEmployessForm(request.POST)
        if form.is_valid():
            user = form.save()
            form = AddEmployessForm()     
            
    else:
        form = AddEmployessForm()
    return render(request, 'add_employee.html', {'form':form})

# Employee Details
@staff_member_required
def employee_details(request):
    if request.user.is_authenticated:
        emp_data = Employee.objects.all()
        user = request.user
        full_name = user.get_full_name()
        return render(request, 'employee_details.html', {'data':emp_data})
    else:
        return HttpResponseRedirect('/')

# Add Attendance
@staff_member_required
def add_attendance(request):
    if request.method == "POST":
        form = AddAttendanceForm(request.POST)
        if form.is_valid():
            user = form.save()
            form = AddAttendanceForm()     
            
    else:
        form = AddAttendanceForm()
    return render(request, 'add_attendance.html', {'form':form})

# View Attendance
@staff_member_required
def attendance_details(request):
    if request.user.is_authenticated:
        att_data = Attendance.objects.all()
        return render(request, 'attendance_details.html', {'data':att_data})
    else:
        return HttpResponseRedirect('/')

# Update Attendance
@staff_member_required
def update_attendance(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Attendance.objects.get(pk=id)
            form = AddAttendanceForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = Attendance.objects.get(pk=id)
            form = AddAttendanceForm(instance=pi)
        return render(request, 'update_attendance.html',{'form':form})
    else:
        return HttpResponseRedirect('/')

# View Employee Applied For Leaves
@staff_member_required
def leave_details(request):
    data = Leave.objects.all()
    return render(request, 'emp_leave_details.html', {'data':data})

# Logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')





def delete_employee(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Employee.objects.get(pk=id)
            pi.delete()
            print('done')
        return HttpResponseRedirect('/employee_details/')
    else:
        return HttpResponseRedirect('/admin_login')