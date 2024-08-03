from django.db import models
from products.models import Product
from crm_system.settings import MEDIA_ROOT


class Contract(models.Model):
    """Модель контракта с клиентом."""
    
    class Meta:
        ordering = ['-start_date']
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Name')
    product = models.ForeignKey(Product, related_name='contracts', on_delete=models.PROTECT, verbose_name='Product')
    contract_file = models.FileField(upload_to=MEDIA_ROOT, verbose_name='Contract file')
    start_date = models.DateTimeField(blank=False, null=False, verbose_name='Contract singing date')
    end_date = models.DateTimeField(blank=False, null=False, verbose_name='Contract expire date')
    cost = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False, verbose_name='Cost')
    