from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django import http
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout

def Registration(request, formName):
    if request.method == 'POST':
        form = formName(request.POST)
        if form.is_valid():
            password = request.POST['password']
            f1 = form.save(commit=False)
            f1.password = make_password(password)
            f1.re_password = f1.password
            f1.save()
