# Generated by Django 3.1.7 on 2021-04-19 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0015_auto_20210419_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorschedule',
            name='day',
            field=models.DateField(null=True),
        ),
    ]
