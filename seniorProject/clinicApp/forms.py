from .models import *
from django import forms
from django.contrib.admin.widgets import AdminTimeWidget


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

