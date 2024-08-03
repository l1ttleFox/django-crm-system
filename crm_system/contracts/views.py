from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Contract
from django.urls import reverse_lazy
from .forms import ContractForm


class ContractCreateView(PermissionRequiredMixin, CreateView):
    """View для создания контракта."""

    model = Contract
    template_name = 'contracts/contracts-create.html'
    form_class = ContractForm
    permission_required = 'contracts.add_contract'
    
    
class ContractDetailView(PermissionRequiredMixin, DetailView):
    """View для просмотра контракта."""

    model = Contract
    template_name = 'contracts/contracts-detail.html'
    permission_required = 'contracts.view_contract'


class ContractListView(PermissionRequiredMixin, ListView):
    """View для просмотра всех контрактов."""

    model = Contract
    template_name = 'contracts/contracts-list.html'
    context_object_name = 'contracts'
    permission_required = 'contracts.view_contract'

    
class ContractUpdateView(PermissionRequiredMixin, UpdateView):
    """View для обновления контракта."""

    model = Contract
    template_name = 'contracts/contracts-edit.html'
    form_class = ContractForm
    permission_required = 'contracts.change_contract'

    
class ContractDeleteView(PermissionRequiredMixin, DeleteView):
    """View для удаления контракта."""

    model = Contract
    template_name = 'contracts/contracts-delete.html'
    success_url = reverse_lazy('contracts:delete')
    permission_required = 'contracts.delete_contract'
