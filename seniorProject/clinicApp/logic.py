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

logger = logging.getLogger('django')

class days(Enum):
    Monday      = "Monday"
    Tuesday     = "Tuesday"
    Wednesday   = "Wednesday"
    Thursday    = "Thursday"
    Friday      = "Friday"
    Saturday    = "Saturday"
    Sunday      = "Sunday"

def Registration(request, formName, modelName):
    if request.method == 'POST':
        logger.info(request.POST)
        email = request.POST['email']
        emCheck = modelName.objects.filter(email = email)
        if not emCheck:
            form = formName(request.POST)
            if form.is_valid():
                password = request.POST['password']
                f1 = form.save(commit=False)
                f1.password = make_password(password)
                f1.re_password = f1.password
                f1.save()

                id = modelName.objects.filter(email = email).values_list('id', flat=True)
                for d in days:
                   crt = DoctorSchedule.objects.create(day=d.value, from_hour='00:00:00', to_hour='00:00:00', doctor_id=id[0])
                   crt.save()
                    #doing bulk insert
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

        except Exception as e:
            http_status_code = 500
            message = "something went wrong"
            logger.error('Unsuccessful login due to ', e)

    data = {"message": message, "id": userID[0]}
    return JsonResponse(data, status=http_status_code)

