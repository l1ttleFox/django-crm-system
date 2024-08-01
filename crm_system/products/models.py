from django.db import models


class Product(models.Model):
    class Meta:
        ordering = ['pk']
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Service name')
    description = models.TextField(blank=True, null=False, verbose_name='Service description')
    cost = models.DecimalField(max_digits=8, decimal_places=2, null=False, verbose_name='Service price')
