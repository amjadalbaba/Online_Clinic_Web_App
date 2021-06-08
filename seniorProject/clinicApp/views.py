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
from .utils import scheduleInsert, checkDay, transfromTimeToInt, halfSplit, timeListItem
from .logic import *
import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Case, When, IntegerField



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
   # TODO: checking why the res.pid is not working
   response = loginAPI(request, Patient)
   # if response.status_code == 200: #we must take the message and decode to redirect
   #     return redirect("userview")
   return response


def loginDoctorPage(request):
    #TODO: checking why the res.pid is not working
    response = loginAPI(request, Doctor)
    return response

#@login_required(login_url='/login-d/')
def d_home(request, pk):
    drl = DoctorSchedule.objects.filter(doctor_id =  pk)
    drl2 = Doctor.objects.get(id = pk)
    drApp = Appointments.objects.filter(doctor_id =  pk).order_by('day')
    logger.info(drApp)


    context = {'list' : drl, 'list2' : drl2,'Appointments': drApp ,'id' : pk}
    return render(request, 'd_dashboard.html', context)

#@login_required(login_url='/api/login-p/')
def p_home(request, pk):
    pt = Patient.objects.get(id = pk)
    ptAppointments = Appointments.objects.filter(patient_id =  pk).order_by('day')

    count  = Appointments.objects.filter(patient_id=pk).count()
    countConsulted = Appointments.objects.filter(checkPrescription='yes').count()

    context = {'patient' : pt, 'id' : pk, 'appointments' : ptAppointments, 'count' : count, 'countConsulted' : countConsulted}
    return render(request, 'p_dashboard.html', context)

#@login_required(login_url='login_d')
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

#@login_required(login_url='/login-d/')
def takeAppointment(request, pk):
    drlist = Doctor.objects.all()

    context = {'doctorList' : drlist,'id' : pk}
    return render(request, 'takeAppointment.html', context)

def loadSchedule(request):
    message = ''
    if request.method == 'GET':
        doctor = request.GET.get('doctor')
        date = request.GET.get('day')
        day = checkDay(date)

        timeList = getScheduleSlots(doctor, day, date)
        return JsonResponse({"doctor": doctor, "day": day, "data": list(timeList)}, safe=False)


    if request.method == 'POST':


        doctor = request.POST.get('doctor')
        date = request.POST.get('day')
        patient = request.POST.get('patient')
        appDay = request.POST.get('day')
        desc = request.POST.get('description')
        day = checkDay(date)

        timeList = getScheduleSlots(doctor, day, date)
        message = 'OK'
        for i in timeList:
            if str(i['idx']) == request.POST['time']:
                 checkTime = Appointments.objects.filter(day=appDay,from_hour=str(i['from']), to_hour=str(i['to']), doctor_id=doctor)
                 if not checkTime:
                     crt = Appointments.objects.create(day=appDay, description=desc, from_hour=str(i['from']), to_hour=str(i['to']), doctor_id=doctor, patient_id= patient)
                     crt.save()
                     crt2 = Consultation.objects.create(appointment_id = crt.id)
                     crt2.save()
                     logger.info(crt.id)
                     message = 'OK'
                 else:
                     message = "Doctor have an appointment at that time, please choose different time range"

    return JsonResponse({"message" : message}, safe=False)

def prescriptionPage(request, pk):
    info = Appointments.objects.get(id = pk)
    doctor = info.doctor.id
    context = {'id' : pk, 'doctor': doctor}

    return render(request, "prescription.html", context)

def addPrescription(request, pk):
    message = 'OK'
    if request.method == 'POST':
        appointmentConsult = Consultation.objects.get(appointment_id = pk)
        appointment = Appointments.objects.get(id = pk)
        logger.info(appointmentConsult)
        if appointmentConsult and appointment:
            appointmentConsult.prescription = request.POST.get('prescript')
            appointmentConsult.price = request.POST.get('price')
            appointmentConsult.drugName = request.POST.get('drugName')

            appointment.checkPrescription = 'yes'

            appointmentConsult.save()
            appointment.save()

        else:
            message = "Doctor have an appointment at that time, please choose different time range"

    return JsonResponse({"message": message}, safe=False)

def appointmentDetailsPage(request, pk, pk2):
    appointmentDetails = Consultation.objects.get(appointment_id = pk)

    context = {'idC' : pk, 'idP' : pk2, 'details': appointmentDetails}

    return render(request, "appointmentDetails.html", context)