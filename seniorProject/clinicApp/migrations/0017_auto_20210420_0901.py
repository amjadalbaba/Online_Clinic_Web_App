# Generated by Django 3.1.7 on 2021-04-20 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0016_auto_20210419_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorschedule',
            name='day',
            field=models.CharField(max_length=100, null=True),
        ),
    ]