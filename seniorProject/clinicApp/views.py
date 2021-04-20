from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache

from django.forms import inlineformset_factory

from .serializers import patientLoginSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

import logging
import json
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .logic import *



logger = logging.getLogger('django')

# Create your views here.

def welcomePage(request):
    context = {}
    return render(request, 'welcome.html', context)

@never_cache
def registerPatientPage(request):

    Registration(request, PatientForm, Patient)
    context = {}
    return render(request, 'register_patient.html', context)


@never_cache
def registerDoctorPage(request):

    Registration(request, DoctorForm, Doctor)
    specialities = Speciality.objects.all()

    context = {
        'specialities' : specialities
               }
    return render(request, 'register_doctor.html', context)

def loginPatPage(request):
    return render(request, "login_patient.html")

def loginDrPage(request):
    return render(request, "login_doctor.html")


def loginPatientPage(request):
   response = loginAPI(request, Patient)
   return response


def loginDoctorPage(request):
    response = loginAPI(request, Doctor)
    return response

def d_home(request):
    context = {}
    return render(request, 'd_dashboard.html', context)

def createSchedule(request, pk):
    # scheduleFormSet = inlineformset_factory(Doctor, DoctorSchedule, fields=('from_hour', 'to_hour', 'day'), extra=7, can_delete=False)
    # logger.info(scheduleFormSet)
    drl = DoctorSchedule.objects.filter(doctor_id = pk)
    logger.info(drl.values('doctor_id', 'from_hour', 'to_hour', 'day'))
    # formset = scheduleFormSet(instance = dr)



    # if request.method == "POST":
    #      formset = scheduleFormSet(request.POST, instance=dr)
    #      logger.info(request.POST)
    #      if formset.is_valid():
    #
    #          formset.save()
    #          return redirect('d_home')

    context = {'list' : drl.values('doctor_id', 'from_hour', 'to_hour', 'day')}
    return render(request, 'schedule.html', context)


