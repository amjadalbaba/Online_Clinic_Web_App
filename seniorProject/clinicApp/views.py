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

def d_home(request, pk):
    drl = DoctorSchedule.objects.filter(doctor_id =  pk)
    for l in drl:
        logger.info(l.from_hour)
    drl2 = Doctor.objects.get(id = pk)

    context = {'list' : drl, 'list2' : drl2, 'id' : pk}
    return render(request, 'd_dashboard.html', context)

def p_home(request, pk):
    pt = Patient.objects.get(id = pk)
    ptAppointments = Appointments.objects.filter(patient_id =  pk)
    context = {'patient' : pt, 'id' : pk, 'appointments' : ptAppointments}
    return render(request, 'p_dashboard.html', context)

def createSchedule(request, pk):

    drl = DoctorSchedule.objects.raw("SELECT id, doctor_id, TIME_FORMAT(from_hour, '%%H:%%i'), TIME_FORMAT(to_hour, '%%H:%%i'), day FROM clinicApp_doctorschedule WHERE doctor_id = " + pk)

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


    context = {'list' : drl, 'id' : pk}
    return render(request, 'schedule.html', context)


def takeAppointment(request, pk):
    drlist = Doctor.objects.all()
    if request.method == 'POST':
        dr = request.POST["doctor"]
        fh = request.POST["from_hour"]
        th = request.POST["to_hour"]
        day = request.POST["day"]
        checkTime = Appointments.objects.filter(doctor=dr, from_hour=fh, to_hour=th, day=day)
        if not checkTime:
             logger.info(request.POST)
             form = AppointmentsForm(request.POST)
             logger.info(form.errors)

             if form.is_valid():
                 form.save()
        else:
             messages.info(request, "Doctor have an appointment at that time, please choose different time range")

    context = {'doctorList' : drlist,'id' : pk}
    return render(request, 'takeAppointment.html', context)