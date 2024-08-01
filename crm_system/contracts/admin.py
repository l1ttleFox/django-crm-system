from django.contrib import admin
from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product', 'start_date', 'end_date', 'cost')
    fields = ('name', 'product', 'contract_file', 'start_date', 'end_date', 'cost')
