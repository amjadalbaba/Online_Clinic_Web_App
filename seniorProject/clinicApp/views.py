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

    Registration(request, PatientForm)
    context = {}
    return render(request, 'register_patient.html', context)


@never_cache
def registerDoctorPage(request):

    Registration(request, DoctorForm)
    specialities = Speciality.objects.all()

    context = {
        'specialities' : specialities
               }
    return render(request, 'register_doctor.html', context)

def loginPatPage(request):
    return render(request, "login_patient.html")

def loginDrPage(request):
    return render(request, "login_doctor.html")


#@api_view(['POST'])
def loginPatientPage(request):
    if request.is_ajax and request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        userAuth = Patient.objects.filter(email=email).values_list('password', flat=True)

        http_status_code = 200
        message = "OK"

        try:
            if not userAuth or not check_password(password, userAuth[0]):
                logger.warning('Patient unsuccessful login due to wrong email or password')
                message = "wrong username or password"

        except Exception as e:
            http_status_code = 500
            message = "something went wrong"
            logger.error('Patient unsuccessful login due to ', e)

    return JsonResponse({"message": message}, status=http_status_code)


# @never_cache
def loginDoctorPage(request):
    if request.is_ajax and request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        userAuth = Doctor.objects.filter(email=email).values_list('password', flat=True)

        http_status_code = 200
        message = "OK"

        try:
            if not userAuth or not check_password(password, userAuth[0]):
                logger.warning('Doctor unsuccessful login due to wrong email or password')
                message = "wrong username or password"

        except Exception as e:
            http_status_code = 500
            message = "something went wrong"
            logger.error('Doctor unsuccessful login due to ', e)

    return JsonResponse({"message": message}, status=http_status_code)
    #return HttpResponse({ "message": message}, status=http_status_code)

def home(request):
    context = {}
    return render(request, 'dashboard.html', context)