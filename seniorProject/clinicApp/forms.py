from .models import *
from django import forms

class DoctorFrom(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientFrom(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorScheduleFrom(forms.ModelForm):
    class Meta:
        model = DoctorSchedule
        fields = '__all__'

class AppointmentsFrom(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = '__all__'

class ConsultationFrom(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = '__all__'

