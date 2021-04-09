from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout




# Create your views here.

def welcomePage(request):
    context = {}
    return render(request, 'welcome.html', context)

def registerPatientPage(request):
    form = PatientForm()
    if request.method == 'POST':
        if request.POST.get('password') != request.POST.get('re_password'):
            messages.info(request, "Please enter the same password in both fields")
            return render(request, 'register_patient.html')
        else:
            form = PatientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login_p')

    context = {'form': form}
    return render(request, 'register_patient.html', context)

def registerDoctorPage(request):
    form = DoctorForm()
    if request.method == 'POST':
        if request.POST.get('password') != request.POST.get('re_password'):
            messages.info(request, "Please enter the same password in both fields")
            return render(request, 'register_doctor.html')
        else:
            form = DoctorForm(request.POST)
            if form.is_valid():
                password = request.POST['password']
                #re_password = request.POST['re_password']
                f1 = form.save(commit=False)
                f1.password = make_password(password)
                f1.re_password = f1.password
                f1.save()
                # if check_password(request.POST['password'], f1.password):
                #     print("successful")
                return redirect('login_d')

    specialities = Speciality.objects.only('specialityName')

    context = {
        'form' : form,
        'specialities' : specialities
               }
    return render(request, 'register_doctor.html', context)

def loginPatientPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        userAuth = Doctor.objects.filter(email = email).values_list('password', flat=True)
        r = userAuth[0]
        print(r)
        # pwdAuth = Doctor.objects.get(password = password)
        if check_password(password, r):
            print("unsuccessful")
        #patient = authenticate(request, email=email, password=password)

        # if patient is not None:
        #     login(request, patient)
        #     return redirect('home')
        # else:
        #     messages.info(request, "username or password is incorrect")
        #     return render(request, 'login.html')


    context = {}
    return render(request, 'login_patient.html', context)

def loginDoctorPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        userAuth = Doctor.objects.filter(email = email).values_list('password', flat=True)
        r = userAuth[0]
        print(r)
        if check_password(password, r):
            print("successful")
            return redirect('home')

    context = {}
    return render(request, 'login_doctor.html', context)

def home(request):
    context = {}
    return render(request, 'dashboard.html', context)