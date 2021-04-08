from .models import *
from django import forms

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
        fields = '__all__'

class AppointmentsForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = '__all__'

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = '__all__'

