from .models import *
from django import forms
from django.contrib.admin.widgets import AdminTimeWidget
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorScheduleForm(forms.ModelForm):
    class Meta:
        model = DoctorSchedule
        fields = ['day', 'from_hour', 'to_hour', 'doctor']

class AppointmentsForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['day', 'from_hour', 'to_hour', 'doctor', 'description', 'patient']

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = '__all__'


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
