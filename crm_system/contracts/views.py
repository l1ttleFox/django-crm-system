from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Contract
from django.urls import reverse_lazy
from .forms import ContractForm


class ContractCreateView(CreateView):
    model = Contract
    template_name = 'contracts/contracts-create.html'
    form_class = ContractForm
    
    
class ContractDetailView(DetailView):
    model = Contract
    template_name = 'contracts/contracts-detail.html'


class ContractListView(ListView):
    model = Contract
    template_name = 'contracts/contracts-list.html'
    context_object_name = 'contracts'
    
    
class ContractUpdateView(UpdateView):
    model = Contract
    template_name = 'contracts/contracts-edit.html'
    form_class = ContractForm
    
    
class ContractDeleteView(DeleteView):
    model = Contract
    template_name = 'contracts/contracts-delete.html'
    success_url = reverse_lazy('contracts:delete')
    