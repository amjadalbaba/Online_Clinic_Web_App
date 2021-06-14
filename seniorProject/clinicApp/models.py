from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


# Create your models here.
class Speciality(models.Model):
    specialityName       = models.CharField(max_length=200, null=True)
    description          = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.specialityName

class Doctor(models.Model):
    firstName            = models.CharField(max_length=200, null=True) #this will haelp in mapping through db
    middleName           = models.CharField(max_length=200, null=True) #it can be empty
    lastName             = models.CharField(max_length=200, null=True)
    email                = models.CharField(max_length=200, null=True)
    address              = models.CharField(max_length=200, null=True)
    phone                = models.CharField(max_length=200, null=True)
    gender               = models.CharField(max_length=200, null=True)
    specialityName       = models.ForeignKey(Speciality, null=True, on_delete=models.SET_NULL)
    password             = models.CharField(max_length=200, null=True)
    created_at           = models.DateTimeField(auto_now_add=True,  null=True)
    updated_at           = models.DateTimeField(auto_now_add=True,  null=True)

    def __str__(self):
        return self.firstName

class Patient(models.Model):
    firstName            = models.CharField(max_length=200, null=True) #this will haelp in mapping through db
    middleName           = models.CharField(max_length=200, null=True) #it can be empty
    lastName             = models.CharField(max_length=200, null=True)
    email                = models.CharField(max_length=200, null=True)
    address              = models.CharField(max_length=200, null=True)
    phone                = models.CharField(max_length=200, null=True)
    gender               = models.CharField(max_length=200, null=True)
    password             = models.CharField(max_length=200, null=True)
    created_at           = models.DateTimeField(auto_now_add=True,  null=True)
    updated_at           = models.DateTimeField(auto_now_add=True,  null=True)

    def __str__(self):
        return self.firstName

@receiver(post_save, sender= settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class DoctorSpeciality(models.Model):
    speciality    = models.ForeignKey(Speciality, null=True, on_delete=models.SET_NULL)
    doctor        = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)

class DoctorSchedule(models.Model):
    doctor              = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    from_hour           = models.TimeField(null=True)
    to_hour             = models.TimeField(null=True)
    day                 = models.CharField(max_length=100, null=True)
    created_at          = models.DateTimeField(auto_now_add=True, null=True)
    updated_at          = models.DateTimeField(auto_now_add=True, null=True)



class Appointments(models.Model):
    doctor              = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    patient             = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    day                 = models.DateField(null=True)
    from_hour           = models.TimeField(null=True)
    to_hour             = models.TimeField(null=True)
    description         = models.CharField(max_length=600, null=True)
    accepted            = models.IntegerField(null=True)
    checkPrescription   = models.CharField(max_length=50, null=True)
    created_at          = models.DateTimeField(auto_now_add=True, null=True)
    updated_at          = models.DateTimeField(auto_now_add=True, null=True)

class Drugs(models.Model):
    drugName             = models.CharField(max_length=200, null=True)
    description          = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.drugName

class Consultation(models.Model):
    appointment         = models.ForeignKey(Appointments, null=True, on_delete=models.SET_NULL)
    prescription        = models.CharField(max_length=200, null=True)
    drugName            = models.CharField(max_length=200, null=True)
    price               = models.CharField(max_length=50, null=True)
    created_at          = models.DateTimeField(auto_now_add=True, null=True)
    updated_at          = models.DateTimeField(auto_now_add=True, null=True)

class doctorReminders(models.Model):
    doctor              = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    content             = models.CharField(max_length=200, null=True)
    sent_at             = models.DateTimeField(auto_now_add=True, null=True)
    retry_count         = models.IntegerField(null=True)
    created_at          = models.DateTimeField(auto_now_add=True, null=True)
    updated_at          = models.DateTimeField(auto_now_add=True, null=True)

class patientReminders(models.Model):
    patient             = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    content             = models.CharField(max_length=200, null=True)
    sent_at             = models.DateTimeField(auto_now_add=True, null=True)
    retry_count         = models.IntegerField(null=True)
    created_at          = models.DateTimeField(auto_now_add=True, null=True)
    updated_at          = models.DateTimeField(auto_now_add=True, null=True)
