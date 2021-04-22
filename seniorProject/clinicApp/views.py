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
from .utils import scheduleInsert
from .logic import *
import datetime


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

    dr  = Doctor.objects.get(id = pk)
    drl = DoctorSchedule.objects.filter(doctor_id = pk)

    logger.info(drl[0].doctor_id)


    if request.method == "POST":
        # logger.info(request.POST)
        # for key in request.POST:
        #     for v in request.POST.getlist(key):
        #           logger.info(v)

        idLst  = request.POST.getlist('doctor')
        dayLst  = request.POST.getlist('day')
        lsf = request.POST.getlist('from_hour')
        lst = request.POST.getlist('to_hour')

        dict = scheduleInsert(idLst, dayLst, lsf, lst)

        for objs,i in zip(drl, range(7)):
            objs.day = dict[i]['day']
            objs.doctor_id = dict[i]['id']
            objs.from_hour = dict[i]['from']
            objs.to_hour = dict[i]['to']
            objs.updated_at = datetime.datetime.now()
            objs.save()

        return redirect('d_home')

    context = {'list' : drl.values('doctor_id', 'from_hour', 'to_hour', 'day'), 'id' : pk}
    return render(request, 'schedule.html', context)


