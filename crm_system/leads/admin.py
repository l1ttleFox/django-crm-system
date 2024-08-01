from django.contrib import admin
from contracts.models import Contract
from customers.models import Customer
from leads.models import Lead


class CustomerInline(admin.TabularInline):
    model = Customer


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'advertising_campaign',
    )
    fields = (
        'first_name',
        'last_name',
        'phone_number',
        'email',
        'advertising_campaign',
    )
    inlines = [
        CustomerInline,
    ]
