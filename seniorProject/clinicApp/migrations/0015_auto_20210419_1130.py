# Generated by Django 3.1.7 on 2021-04-19 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0014_auto_20210419_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorschedule',
            name='from_hour',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='doctorschedule',
            name='to_hour',
            field=models.TimeField(null=True),
        ),
    ]
