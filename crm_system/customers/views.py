from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Customer
from django.urls import reverse_lazy
from .forms import CustomerForm


class CustomerCreateView(PermissionRequiredMixin, CreateView):
    """View для перевода потенциального клиента в активного."""

    model = Customer
    template_name = 'customers/customers-create.html'
    form_class = CustomerForm
    permission_required = 'customers.add_contract'

class CustomerDetailView(PermissionRequiredMixin, DetailView):
    """View для просмотра активного клиента."""

    model = Customer
    template_name = 'customers/customers-detail.html'
    permission_required = 'customers.view_contract'


class CustomerListView(PermissionRequiredMixin, ListView):
    """View для просмотра всех активных клиентов."""

    model = Customer
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'
    permission_required = 'customers.view_contract'


class CustomerUpdateView(PermissionRequiredMixin, UpdateView):
    """View для обновления активного клиента."""

    model = Customer
    template_name = 'customers/customers-edit.html'
    form_class = CustomerForm
    permission_required = 'customers.change_contract'


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    """View для удаления активного клиента."""
    
    model = Customer
    template_name = 'customers/customers-delete.html'
    success_url = reverse_lazy('contracts:delete')
    permission_required = 'customers.delete_contract'
