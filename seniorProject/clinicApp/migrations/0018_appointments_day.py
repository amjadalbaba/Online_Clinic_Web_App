# Generated by Django 3.1.7 on 2021-04-28 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0017_auto_20210420_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='day',
            field=models.TimeField(null=True),
        ),
    ]
