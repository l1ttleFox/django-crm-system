from django.forms import ModelForm
from .models import Lead


class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'advertising_campaign',
        ]
