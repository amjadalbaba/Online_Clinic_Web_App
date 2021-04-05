from django.shortcuts import render, redirect

# Create your views here.

def welcomePage(request):
    context = {}
    return render(request, 'welcome.html', context)

def registerPatientPage(request):
    context = {}
    return render(request, 'register_patient.html', context)

def registerDoctorPage(request):
    context = {}
    return render(request, 'register_doctor.html', context)

def loginPage(request, t):
    context = {}
    return render(request, 'login.html', context)