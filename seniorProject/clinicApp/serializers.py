from rest_framework import serializers
from .models import *

class SpecialitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = '__all__'