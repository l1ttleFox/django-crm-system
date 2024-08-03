from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Lead
from django.urls import reverse_lazy
from .forms import LeadForm


class LeadMixin:
    """Mixin для одинаковых полей в CBV для модели Lead."""
    model = Lead
    form_class = LeadForm
    success_url = reverse_lazy('leads:list')
    
    
class LeadCreateView(LeadMixin, PermissionRequiredMixin, CreateView):
    """View для создания потенциального клиента."""
    template_name = 'leads/leads-create.html'
    permission_required = 'leads.add_lead'


class LeadDetailView(LeadMixin, PermissionRequiredMixin, DetailView):
    """View для просмотра потенциального клиента."""
    template_name = 'leads/leads-detail.html'
    permission_required = 'leads.view_lead'


class LeadListView(LeadMixin, PermissionRequiredMixin, ListView):
    """View для просмотра всех потенциальных клиентов."""
    template_name = 'leads/leads-list.html'
    context_object_name = 'leads'
    permission_required = 'leads.view_lead'


class LeadUpdateView(LeadMixin, PermissionRequiredMixin, UpdateView):
    """View для обновления потенциального клиента."""
    template_name = 'leads/leads-edit.html'
    permission_required = 'leads.edit_lead'


class LeadDeleteView(LeadMixin, PermissionRequiredMixin, DeleteView):
    """View для удаления потенциального клиента."""
    template_name = 'leads/leads-delete.html'
    permission_required = 'leads.delete_lead'
