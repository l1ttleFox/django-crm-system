from django.db import models
from products.models import Product


class Advertisement(models.Model):
    """Модель рекламной кампании."""
    
    class Meta:
        ordering = ['pk']
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False, verbose_name='Advertisement campaign name')
    product = models.ForeignKey(Product, related_name='advertisements', on_delete=models.CASCADE, verbose_name='Product to be promoted')
    promotion_channel = models.CharField(max_length=200, blank=False, null=False, verbose_name='Promotion channel')
    budget = models.DecimalField(max_digits=8, decimal_places=2, null=False, verbose_name='Advertisement budget')
    