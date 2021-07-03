from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django import http
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
import logging
from rest_framework.response import Response
from enum import Enum

from django.http import JsonResponse
from .utils import *

logger = logging.getLogger('django')
halfhour = 30

class days(Enum):
    Monday      = "Monday"
    Tuesday     = "Tuesday"
    Wednesday   = "Wednesday"
    Thursday    = "Thursday"
    Friday      = "Friday"
    Saturday    = "Saturday"
    Sunday      = "Sunday"

def Registration(request):
    if request.method == 'POST':
        email = request.POST['email']
        emCheck = User.objects.filter(email = email)
        logger.info(request.POST['Regtype'])

        if not emCheck:
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                logger.info(request.POST['Regtype'])

                if str(request.POST['Regtype']) == str('dr'):
                    id = User.objects.filter(email=email).values_list('id', flat=True)
                    logger.info(id[0])
                    f1 = Doctor.objects.create(user_id=id[0], gender=request.POST['gender'], address=request.POST['address'], phone=request.POST['phone'], specialityName_id=request.POST['specialityName'])
                    f1.save()
                    id = Doctor.objects.filter(user_id=id[0]).values_list('id', flat=True)
                    for d in days:
                        crt = DoctorSchedule.objects.create(day=d.value, from_hour='00:00:00', to_hour='00:00:00',
                                                            doctor_id=id[0])
                        crt.save()
                else:
                    id = User.objects.filter(email=email).values_list('id', flat=True)
                    f1 = Patient.objects.create(user_id=id[0], gender=request.POST['gender'],
                                               address=request.POST['address'], phone=request.POST['phone'])
                    f1.save()

                # usern = form.cleaned_data['username']
                # pwd = form.cleaned_data['password1']
                # user = authenticate(username=usern, password=pwd)
                # login(request, user)
                # return redirect('p_home')
            else:
                messages.info(request,form.errors)


        else:
            messages.info(request, "email exists")


def loginAPI(request, formName):
    if request.is_ajax and request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        userAuth = formName.objects.filter(email=email).values_list('password', flat=True)

        http_status_code = 200
        message = "OK"
        userID = ['']

        try:
            if not userAuth or not check_password(password, userAuth[0]):
                logger.warning('Unsuccessful login due to wrong email or password')
                message = "wrong email or password"

            else:
                userID = formName.objects.filter(email=email).values_list('id', flat=True)
                message = "OK"
                request.session['userID'] = userID[0]

        except Exception as e:
            http_status_code = 500
            message = "something went wrong"
            logger.error('Unsuccessful login due to ', e)

    data = {"message": message, "id": userID[0]}
    return JsonResponse(data, status=http_status_code)


def getDoctorFreeSlots(doctor, day, date):
    """
    :param doctor: doctor_id
    :param day: day of chosen appointment to take
    :param date: date of appointment
    :return: return a list of the remaining free time slots for a patient to take an appointment
    """
    doctorStartingHour = DoctorSchedule.objects.filter(doctor_id=doctor).filter(day=day).values_list('from_hour', flat=True)
    doctorEndHour = DoctorSchedule.objects.filter(doctor_id=doctor).filter(day=day).values_list('to_hour', flat=True)

    doctorAppointmentStartingHour = Appointments.objects.filter(doctor_id=doctor).filter(day=date).values_list('from_hour', flat=True)


    listOfDoctorStartAppointmentsHour = []

    for i in range(0,len(doctorAppointmentStartingHour)):
        if doctorAppointmentStartingHour[i].minute == halfhour:
            listOfDoctorStartAppointmentsHour.append(doctorAppointmentStartingHour[i].hour + 0.5) # if we have for example 20:30
        else:
            listOfDoctorStartAppointmentsHour.append(doctorAppointmentStartingHour[i].hour)
    logger.info(listOfDoctorStartAppointmentsHour)


    for i in range(0,len(listOfDoctorStartAppointmentsHour)):
            listOfDoctorStartAppointmentsHour.append(listOfDoctorStartAppointmentsHour[i] + 0.5)

    listOfDoctorStartAppointmentsHour = list(set(listOfDoctorStartAppointmentsHour))
    logger.info(listOfDoctorStartAppointmentsHour)


    slist = halfSplit(doctorStartingHour[0].hour, doctorEndHour[0].hour)
    logger.info(slist)


    slist = [x for x in slist if x not in listOfDoctorStartAppointmentsHour]


    logger.info(slist)

    if len(slist) == 0:
        timeList = {}
    else:
        timeList = timeListItem(slist)

    return timeList


