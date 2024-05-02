# Generated by Django 5.0 on 2024-05-01 12:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0001_initial'),
        ('hospital_processes', '0002_remove_surgeries_condition_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnostictests',
            name='condition_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conditions.medicalcondition'),
        ),
    ]