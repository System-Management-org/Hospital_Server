# Generated by Django 4.1.5 on 2024-02-17 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserViews', '0005_remove_patient_registrar'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='registrar_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
