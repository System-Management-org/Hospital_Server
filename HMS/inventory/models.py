from django.db import models

# Create your models here.
class Drugs(models.Model):
    drug_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    Formulation = models.CharField(max_length=250)
    cost = models.FloatField()
    quantity_in_stock = models.IntegerField()