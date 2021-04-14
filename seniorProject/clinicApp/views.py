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

        # pwdAuth = Doctor.objects.get(password = password)
        try:
            if check_password(password, userAuth[0]):
                logger.info('Patient successful login')
                response = json.dumps([{'message':'Successful login.'}])
                return JsonResponse(response, status=200, safe=False)

            else:
                logger.info('Patient unsuccessful login')

        except Exception as e:
            logger.info(e)
            logger.info('Patient unsuccessful login')
            response = json.dumps([{'message':'something went wrong.'}])
            return JsonResponse(response, status=404, safe=False)

    return JsonResponse({"message":"something went wrong."}, status=404, safe=False)


# @never_cache
def loginDoctorPage(request):
    if request.is_ajax and request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        userAuth = Doctor.objects.filter(email=email).values_list('password', flat=True)

        # pwdAuth = Doctor.objects.get(password = password)
        try:
            if check_password(password, userAuth[0]):
                logger.info('Doctor successful login')
                response = json.dumps([{'message': 'Successful login.'}])
                return JsonResponse(response, status=200, safe=False)

            else:
                logger.info('Doctor unsuccessful login')

        except Exception as e:
            logger.info(e)
            logger.info('Doctor unsuccessful login')
            response = json.dumps([{'message': 'something went wrong.'}])
            return JsonResponse(response, status=404, safe=False)

    return JsonResponse({"message": "something went wrong."}, status=404, safe=False)

def home(request):
    context = {}
    return render(request, 'dashboard.html', context)