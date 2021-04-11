from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache

import logging

from .logic import *



logger = logging.getLogger('django')

# Create your views here.

def welcomePage(request):
    context = {}
    return render(request, 'welcome.html', context)

def registerPatientPage(request):

    Registration(request, PatientForm)
    context = {}
    return render(request, 'register_patient.html', context)



def registerDoctorPage(request):

    Registration(request, DoctorForm)
    specialities = Speciality.objects.only('specialityName')

    context = {
        'specialities' : specialities
               }
    return render(request, 'register_doctor.html', context)

def loginPatientPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        userAuth = Patient.objects.filter(email = email).values_list('password', flat=True)

        # pwdAuth = Doctor.objects.get(password = password)
        try:
            if check_password(password, userAuth[0]):
                logger.info('Doctor successful login')
                return redirect('home')
            else:
                messages.info(request, "Email or password is incorrect")
                return render(request, 'login.html')
        except Exception as e:
            logger.info(e)

    context = {}
    return render(request, 'login_patient.html', context)


def loginDoctorPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        userAuth = Doctor.objects.filter(email = email).values_list('password', flat=True)

        try:
            if check_password(password, userAuth[0]):
                logger.info('Doctor successful login')
                return redirect('home')
            else:
                messages.info(request, "Email or password is incorrect")
                return render(request, 'login.html')
        except Exception as e:
            logger.info(e)

    context = {}
    return render(request, 'login_doctor.html', context)

def home(request):
    context = {}
    return render(request, 'dashboard.html', context)