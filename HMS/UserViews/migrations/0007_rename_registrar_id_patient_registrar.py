# Generated by Django 4.1.5 on 2024-02-17 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserViews', '0006_patient_registrar_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='registrar_id',
            new_name='registrar',
        ),
    ]
