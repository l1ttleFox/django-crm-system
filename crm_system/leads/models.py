from django.db import models
from ads.models import Advertisement


class Lead(models.Model):
    """Модель потенциального клиента, привлеченного рекламной кампанией."""
    class Meta:
        ordering = ['pk']
    
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='First name')
    last_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Last name')
    phone_number = models.CharField(max_length=20, blank=True, null=False, verbose_name='Phone number')
    email = models.EmailField(max_length=254, blank=True, null=False, verbose_name='Email')
    advertising_campaign = models.ForeignKey(Advertisement, related_name='leads', on_delete=models.PROTECT, verbose_name='The campaign user came from')
