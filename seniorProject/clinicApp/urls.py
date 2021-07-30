from django.urls import path
from . import logic

urlpatterns = [
    path('', logic.res, name='resc'),
    path('drug-list/', logic.listing, name="drugs"),

]