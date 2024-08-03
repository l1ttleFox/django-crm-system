from django.forms import ModelForm
from .models import Customer


class CustomerForm(ModelForm):
    """View для модели активного клиента."""
    class Meta:
        model = Customer
        fields = [
            'id',
            'lead',
            'contract',
        ]
