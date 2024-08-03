from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Lead
from django.urls import reverse_lazy
from .forms import LeadForm


class LeadCreateView(PermissionRequiredMixin, CreateView):
    """View для создания потенциального клиента."""

    model = Lead
    template_name = 'leads/leads-create.html'
    form_class = LeadForm
    permission_required = 'leads.add_lead'


class LeadDetailView(PermissionRequiredMixin, DetailView):
    """View для просмотра потенциального клиента."""

    model = Lead
    template_name = 'leads/leads-detail.html'
    permission_required = 'leads.view_lead'


class LeadListView(PermissionRequiredMixin, ListView):
    """View для просмотра всех потенциальных клиентов."""

    model = Lead
    template_name = 'leads/leads-list.html'
    context_object_name = 'leads'
    permission_required = 'leads.view_lead'


class LeadUpdateView(PermissionRequiredMixin, UpdateView):
    """View для обновления потенциального клиента."""

    model = Lead
    template_name = 'leads/leads-edit.html'
    form_class = LeadForm
    permission_required = 'leads.edit_lead'


class LeadDeleteView(PermissionRequiredMixin, DeleteView):
    """View для удаления потенциального клиента."""
    
    model = Lead
    template_name = 'leads/leads-delete.html'
    success_url = reverse_lazy('leads:delete')
    permission_required = 'leads.delete_lead'
