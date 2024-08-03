from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    """Форма для модели услуги, предоставляемой компанией."""
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'cost',
        ]
