from .models import *
from datetime import date
import logging
logger = logging.getLogger('django')

def job():
    logger.info('working')
    # c = Drugs.objects.create(drugName= 'tt', description='tt')
    # c.save()

    # dayOfAppointment = str(date.today())
    # checkAppointmentExisting = Appointments.objects.get(day=dayOfAppointment)
    #
    # if checkAppointmentExisting:
    #     patientId = checkAppointmentExisting['patient_id']
    #     doctorId = checkAppointmentExisting['doctor_id']
    #
    #     doctorUserID = Doctor.objects.get(id = doctorId)
    #     patientUserID = Patient.objects.get(id = patientId)
    #
    #     doctorEmail = User.objects.filter(id = doctorUserID).values_list('email', flat=True)
    #     patientEmail = User.objects.filter(id = patientUserID).values_list('email', flat=True)


