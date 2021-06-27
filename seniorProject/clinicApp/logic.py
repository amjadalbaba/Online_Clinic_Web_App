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


def getScheduleSlots(doctor, day, date):
    # get the from,to hour in a certain day in dr schedule
    drTimeFrom = DoctorSchedule.objects.filter(doctor_id=doctor).filter(day=day).values_list('from_hour', flat=True)
    drTimeTo = DoctorSchedule.objects.filter(doctor_id=doctor).filter(day=day).values_list('to_hour', flat=True)

    # get the from,to hour in a certain day in appointments with a certain dr
    drTimeFromApp = Appointments.objects.filter(doctor_id=doctor).filter(day=date).values_list('from_hour', flat=True)
    drTimeToApp = Appointments.objects.filter(doctor_id=doctor).filter(day=date).values_list('to_hour', flat=True)


    l1 = []
    l2 = []


    #1: insert in a list all from_hours from appointments table for a certain dr
    for i in range(0,len(drTimeFromApp)):
        if drTimeFromApp[i].minute != 0:
            l1.append(drTimeFromApp[i].hour + 0.5) # if we have for example 20:30
        else:
            l1.append(drTimeFromApp[i].hour)
    logger.info(l1)


    #insert in a list all from_hours from schedule table for a certain dr
    # for i in range(0,len(drTimeFrom)):
    #     l2.append(drTimeFrom[i].hour)
    # logger.info(l2)


    #2: convert the list all from_hours from appointments table for a certain dr into halfs
    for i in range(0,len(l1)):
        if(((l1[i] + 0.5) in l1)):
             continue
        else:
            l1.append(l1[i] + 0.5)
    logger.info(l1)


    slist = halfSplit(drTimeFrom[0].hour, drTimeTo[0].hour)
    logger.info(slist)

    array_3 = slist
    for x in l1:
        try:
            array_3.remove(x)
        except ValueError:
            pass

    logger.info(array_3)

    if len(array_3) == 0:
        timeList = {}
    else:
        timeList = timeListItem(array_3)


    return timeList

def getFreeSlots(doctor, day):
    drTimeFrom = DoctorSchedule.objects.filter(doctor_id=doctor).filter(day=day).values_list('from_hour', flat=True)
    drTimeFromApp = Appointments.objects.filter(doctor_id=doctor).filter(day=date).values_list('from_hour', flat=True)
