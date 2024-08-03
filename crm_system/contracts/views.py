from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Contract
from django.urls import reverse_lazy
from .forms import ContractForm


class ContractMixin:
    """Mixin для одинаковых полей в CBV для модели Contract."""
    model = Contract
    form_class = ContractForm
    success_url = reverse_lazy('contracts:list')
    
    
class ContractCreateView(ContractMixin, PermissionRequiredMixin, CreateView):
    """View для создания контракта."""
    template_name = 'contracts/contracts-create.html'
    permission_required = 'contracts.add_contract'
    
    
class ContractDetailView(ContractMixin, PermissionRequiredMixin, DetailView):
    """View для просмотра контракта."""
    template_name = 'contracts/contracts-detail.html'
    permission_required = 'contracts.view_contract'


class ContractListView(ContractMixin, PermissionRequiredMixin, ListView):
    """View для просмотра всех контрактов."""
    template_name = 'contracts/contracts-list.html'
    context_object_name = 'contracts'
    permission_required = 'contracts.view_contract'

    
class ContractUpdateView(ContractMixin, PermissionRequiredMixin, UpdateView):
    """View для обновления контракта."""
    template_name = 'contracts/contracts-edit.html'
    permission_required = 'contracts.change_contract'

    
class ContractDeleteView(ContractMixin, PermissionRequiredMixin, DeleteView):
    """View для удаления контракта."""
    template_name = 'contracts/contracts-delete.html'
    permission_required = 'contracts.delete_contract'
