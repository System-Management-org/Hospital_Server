# Generated by Django 5.0 on 2024-05-01 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_remove_hospitalization_patient_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='insurance_id',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='insurance_type',
            field=models.CharField(choices=[('National', 'National'), ('Private', 'Private'), ('None', 'None')], default='None'),
        ),
    ]
