from django.db import models
from leads.models import Lead
from contracts.models import Contract


class Customer(models.Model):
    class Meta:
        ordering = ['pk']
    
    id = models.AutoField(primary_key=True)
    lead = models.ForeignKey(Lead, related_name='customers', on_delete=models.CASCADE, verbose_name='Lead')
    contract = models.OneToOneField(Contract, related_name='customer', on_delete=models.CASCADE, verbose_name='Contract')
    