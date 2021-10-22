from django import forms
from .models import Employee,Attendance, Leave
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _

class AddEmployessForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model = Employee
        fields = ['username','date_of_joining','first_name','middle_name','last_name','email','phone',
        'gender','date_of_birth','nationality','village','address']
        widgets = {'username':forms.TextInput(attrs={'placeholder':'Username'}),
                    'date_of_joining':forms.TextInput(attrs={'placeholder':'DOJ(yyyy-mm-dd)'}),
                    'first_name':forms.TextInput(attrs={'placeholder':'First Name'}),
                    'middle_name':forms.TextInput(attrs={'placeholder':'Middle Name'}),
                    'last_name':forms.TextInput(attrs={'placeholder':'Last Name'}),
                    'email':forms.TextInput(attrs={'placeholder':'Email'}),
                    'phone':forms.TextInput(attrs={'placeholder':'Phone(+911234567890)'}),
                    'date_of_birth':forms.TextInput(attrs={'placeholder':'DOB(yyyy-mm-dd)'}),
                    'nationality':forms.TextInput(attrs={'placeholder':'Nationality'}),
                    'village':forms.TextInput(attrs={'placeholder':'Village'}),
                    'address':forms.TextInput(attrs={'placeholder':'Address'}),
                    
        }
    
class AddAttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['user','attendance_date', 'in_time', 'out_time', 'attendance', 'regularization_status','description']
        widgets = {'description':forms.Textarea(attrs={'placeholder':'Drop your message here'}),
                    'attendance_date':forms.DateInput(attrs={'placeholder':'yyyy-mm-dd'}),
                    'in_time':forms.TimeInput(attrs={'placeholder':'hh:mm:ss'}),
                    'out_time':forms.TimeInput(attrs={'placeholder':'hh:mm:ss'}),
        }

class Emp_AddAttendanceForm(forms.ModelForm):
    user = forms.CharField(widget=forms.HiddenInput(),initial='abc')
    class Meta:
        model = Attendance
        fields = ['attendance_date', 'in_time', 'out_time', 'attendance', 'description']
        widgets = {'description':forms.Textarea(),
        'attendance_date':forms.DateInput(attrs={'placeholder':'yyyy-mm-dd'}),
        'in_time':forms.TimeInput(attrs={'placeholder':'hh:mm:ss'}),
        'out_time':forms.TimeInput(attrs={'placeholder':'hh:mm:ss'}),
        }

class LeaveForm(forms.ModelForm):
    user = forms.CharField(widget=forms.HiddenInput(),initial='abc')
    class Meta:
        model = Leave
        fields = ['from_date', 'from_date_day', 'to_date', 'to_date_day','reason']
        widgets = {'from_date':forms.DateInput(attrs={'placeholder':'yyyy-mm-dd'}),
        'to_date':forms.DateInput(attrs={'placeholder':'yyyy-mm-dd'}),
        'reason':forms.Textarea(attrs={'placeholder':'Valid Reason Only'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
    password = forms.CharField(label=_('password'), strip=False, 
    widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

