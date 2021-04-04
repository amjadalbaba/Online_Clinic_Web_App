from django.shortcuts import render, redirect

# Create your views here.

def registerPage(request):
    context = {}
    return render(request, 'register_patient.html', context)

def loginPage(request):
    context = {}
    return render(request, 'login.html', context)