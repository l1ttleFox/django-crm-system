from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Customer
from django.urls import reverse_lazy
from .forms import CustomerForm


class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customers/customers-create.html'
    form_class = CustomerForm


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customers-detail.html'


class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customers/customers-edit.html'
    form_class = CustomerForm


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customers/customers-delete.html'
    success_url = reverse_lazy('contracts:delete')
