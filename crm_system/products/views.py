from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy
from .forms import ProductForm


class ProductCreateView(PermissionRequiredMixin, CreateView):
    """View для создания услуги."""

    model = Product
    template_name = 'products/products-create.html'
    form_class = ProductForm
    permission_required = 'products.add_product'
    

class ProductDetailView(PermissionRequiredMixin, DetailView):
    """View для просмотра услуги."""
    
    model = Product
    template_name = 'products/products-detail.html'
    permission_required = 'products.view_product'


class ProductListView(PermissionRequiredMixin, ListView):
    """View для просмотра всех услуг."""
    
    model = Product
    template_name = 'products/products-list.html'
    context_object_name = 'products'
    permission_required = 'products.view_product'


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    """View для обновления услуги."""

    model = Product
    template_name = 'products/products-edit.html'
    form_class = ProductForm
    permission_required = 'products.change_product'


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    """View для удаления услуги."""

    model = Product
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('products:delete')
    permission_required = 'products.delete_product'
