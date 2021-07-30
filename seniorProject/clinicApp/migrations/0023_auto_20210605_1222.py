# Generated by Django 3.1.7 on 2021-06-05 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0022_appointments_accepted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='consultation',
            name='patient',
        ),
        migrations.AddField(
            model_name='consultation',
            name='appointment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinicApp.appointments'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='drugName',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
