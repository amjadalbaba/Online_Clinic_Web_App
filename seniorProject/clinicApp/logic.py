from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache

def patientRegistration(request):
    if request.method == 'POST':
        # if request.POST.get('password') == '1':
        #     messages.info(request, "Please enter the same password in both fields")
        #     return render(request, 'register_patient.html')

        form = PatientForm(request.POST)
        if form.is_valid():
            password = request.POST['password']
            # re_password = request.POST['re_password']
            f1 = form.save(commit=False)
            f1.password = make_password(password)
            f1.re_password = f1.password
            f1.save()
            # if check_p
            return redirect('login_p')

def doctorRegistration(request):
    if request.method == 'POST':
        # if request.POST.get('password') == '1':
        #     messages.info(request, "Please enter the same password in both fields")
        #     return render(request, 'register_patient.html')

        form = DoctorForm(request.POST)
        if form.is_valid():
            password = request.POST['password']
            # re_password = request.POST['re_password']
            f1 = form.save(commit=False)
            f1.password = make_password(password)
            f1.re_password = f1.password
            f1.save()
            # if check_p
            return redirect('login_d')