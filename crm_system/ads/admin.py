from django.contrib import admin

from leads.models import Lead
from .models import Advertisement


class LeadInline(admin.TabularInline):
    model = Lead


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'product',
        'promotion_channel',
        'budget',
    )
    fields = (
        'name',
        'product',
        'promotion_channel',
        'budget',
    )
    inlines = [
        LeadInline
    ]