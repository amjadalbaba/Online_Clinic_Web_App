# Generated by Django 3.1.7 on 2021-04-29 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicApp', '0019_auto_20210429_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='description',
            field=models.CharField(max_length=600, null=True),
        ),
    ]
