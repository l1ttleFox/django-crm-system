from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Customer
from django.urls import reverse_lazy
from .forms import CustomerForm


class CustomerMixin:
    """Mixin для одинаковых полей в CBV для модели Customer."""
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('contracts:list')
    
    
class CustomerCreateView(CustomerMixin, PermissionRequiredMixin, CreateView):
    """View для перевода потенциального клиента в активного."""
    template_name = 'customers/customers-create.html'
    permission_required = 'customers.add_contract'


class CustomerDetailView(CustomerMixin, PermissionRequiredMixin, DetailView):
    """View для просмотра активного клиента."""
    template_name = 'customers/customers-detail.html'
    permission_required = 'customers.view_contract'


class CustomerListView(CustomerMixin, PermissionRequiredMixin, ListView):
    """View для просмотра всех активных клиентов."""
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'
    permission_required = 'customers.view_contract'


class CustomerUpdateView(CustomerMixin, PermissionRequiredMixin, UpdateView):
    """View для обновления активного клиента."""
    template_name = 'customers/customers-edit.html'
    permission_required = 'customers.change_contract'


class CustomerDeleteView(CustomerMixin, PermissionRequiredMixin, DeleteView):
    """View для удаления активного клиента."""
    template_name = 'customers/customers-delete.html'
    permission_required = 'customers.delete_contract'
