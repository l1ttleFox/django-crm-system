from django.contrib import admin

from contracts.models import Contract
from .models import Product
from ads.models import Advertisement


class AdvertisementInline(admin.TabularInline):
    model = Advertisement
    

class ContractInline(admin.TabularInline):
    model = Contract


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'cost')
    fields = ('name', 'description', 'cost')
    inlines = [
        AdvertisementInline,
        ContractInline,
    ]
