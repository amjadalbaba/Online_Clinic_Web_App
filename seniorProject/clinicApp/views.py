from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache

from .serializers import patientLoginSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

import logging
import json
from django.http import HttpResponse
from django.http import JsonResponse


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

def home(request):
    context = {}
    return render(request, 'dashboard.html', context)