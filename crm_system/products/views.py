from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy
from .forms import ProductForm


class ProductMixin:
    """Mixin для одинаковых полей в CBV для модели Product."""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:list')
    
    
class ProductCreateView(ProductMixin, PermissionRequiredMixin, CreateView):
    """View для создания услуги."""
    template_name = 'products/products-create.html'
    permission_required = 'products.add_product'
    

class ProductDetailView(ProductMixin, PermissionRequiredMixin, DetailView):
    """View для просмотра услуги."""
    template_name = 'products/products-detail.html'
    permission_required = 'products.view_product'


class ProductListView(ProductMixin, PermissionRequiredMixin, ListView):
    """View для просмотра всех услуг."""
    template_name = 'products/products-list.html'
    context_object_name = 'products'
    permission_required = 'products.view_product'


class ProductUpdateView(ProductMixin, PermissionRequiredMixin, UpdateView):
    """View для обновления услуги."""
    template_name = 'products/products-edit.html'
    permission_required = 'products.change_product'


class ProductDeleteView(ProductMixin, PermissionRequiredMixin, DeleteView):
    """View для удаления услуги."""
    template_name = 'products/products-delete.html'
    permission_required = 'products.delete_product'
