from django.forms import ModelForm
from .models import Advertisement


class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = [
            'id',
            'name',
            'product',
            'promotion_channel',
            'budget',
        ]
