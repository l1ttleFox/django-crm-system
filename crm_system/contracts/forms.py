from django.forms import ModelForm
from .models import Contract


class ContractForm(ModelForm):
    """Форма для модели контракта."""
    class Meta:
        model = Contract
        fields = [
            'id',
            'name',
            'product',
            'contract_file',
            'start_date',
            'end_date',
            'cost',
        ]
