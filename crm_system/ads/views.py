from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Count, Sum, F
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Advertisement
from .forms import AdvertisementForm


class AdvertisementCreateView(PermissionRequiredMixin, CreateView):
    """View для создания рекламы."""
    
    model = Advertisement
    template_name = 'ads/ads-create.html'
    form_class = AdvertisementForm
    permission_required = 'ads.add_advertisement'
    

class AdvertisementDetailView(PermissionRequiredMixin, DetailView):
    """View для просмотра рекламы."""
    
    model = Advertisement
    template_name = 'ads/ads-detail.html'
    permission_required = 'ads.view_advertisement'
    
    
class AdvertisementListView(PermissionRequiredMixin, ListView):
    """View для просмотра всех реклам."""
    
    model = Advertisement
    template_name = 'ads/ads-list.html'
    context_object_name = 'ads'
    permission_required = 'ads.view_advertisement'


class AdvertisementUpdateView(PermissionRequiredMixin, UpdateView):
    """View для обновления рекламы."""
    
    model = Advertisement
    template_name = 'ads/ads-edit.html'
    form_class = AdvertisementForm
    permission_required = 'ads.change_advertisement'


class AdvertisementDeleteView(PermissionRequiredMixin, DeleteView):
    """View для удаления рекламы."""
    
    model = Advertisement
    template_name = 'ads/ads-delete.html'
    success_url = reverse_lazy('ads:list')
    permission_required = 'ads.delete_advertisement'


class AdvertisementStatisticView(ListView):
    """View для просмотра статистики рекламных компаний."""

    template_name = 'ads/ads-statistic.html'
    context_object_name = 'ads'
    
    def get_queryset(self):
        qs = Advertisement.objects.annotate(leads_count=Count('leads'))
        qs = qs.annotate(customers_count=Count('leads__customers'))
        qs = qs.annotate(profit=(Sum('leads__customers__contract__cost') - F('budget')))
        
        return qs
    