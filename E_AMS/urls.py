from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('employee_login/', views.employee_login,name='employee_login'),
    path('employee_dashboard/', views.employee_dashboard,name='employee_dashboard'),
    path('emp_add_attendance/', views.emp_add_attendance, name='emp_add_attendance'),
    path('emp_attendance_details/', views.employee_attendance_details, name='emp_attendance_details'),
    path('employee_leave/', views.leave_view, name='employee_leave'),

    path('admin_login/', views.admin_login,name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard,name='admin_dashboard'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('employee_details/', views.employee_details, name='employee_details'),
    path('delete_employee/<int:id>', views.delete_employee, name='delete_employee'),
    path('add_attendance/', views.add_attendance, name='add_attendance'),
    path('attendance_details/', views.attendance_details, name='attendance_details'),
    path('update_attendance/<int:id>', views.update_attendance, name='update_attendance'),
    path('emp_leave_details/', views.leave_details, name='emp_leave_details'),
    
    path('logout/', views.logout_view,name='logout'),
]
