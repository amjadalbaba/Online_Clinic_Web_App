from rest_framework import serializers
from .models import *

class patientLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'