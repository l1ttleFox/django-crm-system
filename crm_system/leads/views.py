from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Lead
from django.urls import reverse_lazy
from .forms import LeadForm


class LeadCreateView(CreateView):
    model = Lead
    template_name = 'leads/leads-create.html'
    form_class = LeadForm


class LeadDetailView(DetailView):
    model = Lead
    template_name = 'leads/leads-detail.html'


class LeadListView(ListView):
    model = Lead
    template_name = 'leads/leads-list.html'
    context_object_name = 'leads'


class LeadUpdateView(UpdateView):
    model = Lead
    template_name = 'leads/leads-edit.html'
    form_class = LeadForm


class LeadDeleteView(DeleteView):
    model = Lead
    template_name = 'leads/leads-delete.html'
    success_url = reverse_lazy('leads:delete')
