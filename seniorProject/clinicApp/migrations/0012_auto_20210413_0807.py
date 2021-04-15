# Generated by Django 3.1.7 on 2021-04-13 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0011_doctor_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialityName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinicApp.speciality'),
        ),
    ]