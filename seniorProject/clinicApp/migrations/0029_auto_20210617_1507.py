# Generated by Django 3.1.7 on 2021-06-17 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0028_auto_20210617_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='email',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='middleName',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='password',
        ),
    ]