from django.forms import ModelForm
from .models import Advertisement


class AdvertisementForm(ModelForm):
    """Форма для модели рекламы."""
    
    class Meta:
        model = Advertisement
        fields = [
            'id',
            'name',
            'product',
            'promotion_channel',
            'budget',
        ]
