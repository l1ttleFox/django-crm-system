from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy
from .forms import ProductForm


class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/products-create.html'
    form_class = ProductForm


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/products-detail.html'


class ProductListView(ListView):
    model = Product
    template_name = 'products/products-list.html'
    context_object_name = 'products'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/products-edit.html'
    form_class = ProductForm


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('products:delete')
