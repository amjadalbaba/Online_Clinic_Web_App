"""seniorProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from clinicApp import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('register-patient/', views.registerPatientPage, name="register-patient"),
    url('register-doctor/', views.registerDoctorPage, name="register-doctor"),

    path('login-p/', views.loginPatPage, name="login_p"),
    path('logout-p/', views.logoutPatientUser, name="logout_p"),
    path('api/login-p/', views.loginPatientPage, name="login_p_api"),

    path('login-d/', views.loginDoctorPage, name="login_d"),
    path('logout-d/', views.logoutDoctorUser, name="logout_d"),
    path('api/login-d/', views.loginDoctorPagee, name="login_d_api"),

    #path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),


    path('home-d/', views.d_home, name="d_home"),
    path('home-p/', views.p_home, name="p_home"),
    path('', views.welcomePage, name="welcome"),

    path('schedule-d/', views.createSchedule, name="schedule_d"),
    path('appointment-p/', views.takeAppointment, name="appointment_d"),
    path('api/appointment-d/', views.loadSchedule, name="appointment_api"),

    path('prescription/<str:pk>/', views.prescriptionPage, name="prescription"),
    path('api/prescript/<str:pk>/', views.addPrescription, name="prescript_api"),

    path('details/<str:pk>/', views.appointmentDetailsPage, name="details"),


    path('api/', include('clinicApp.urls')),
]

