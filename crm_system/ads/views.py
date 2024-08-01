from django.db.models import Count, Sum, F
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Advertisement
from .forms import AdvertisementForm


class AdvertisementCreateView(CreateView):
    model = Advertisement
    template_name = 'ads/ads-create.html'
    form_class = AdvertisementForm
    

class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'ads/ads-detail.html'
    
    
class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'ads/ads-list.html'
    context_object_name = 'ads'
    

class AdvertisementUpdateView(UpdateView):
    model = Advertisement
    template_name = 'ads/ads-edit.html'
    form_class = AdvertisementForm
    

class AdvertisementDeleteView(DeleteView):
    model = Advertisement
    template_name = 'ads/ads-delete.html'
    success_url = reverse_lazy('ads:list')
    

class AdvertisementStatisticView(ListView):
    template_name = 'ads/ads-statistic.html'
    context_object_name = 'ads'
    
    def get_queryset(self):
        qs = Advertisement.objects.annotate(leads_count=Count('leads'))
        qs = qs.annotate(customers_count=Count('leads__customers'))
        qs = qs.annotate(profit=(Sum('leads__customers__contract__cost') - F('budget')))
        
        return qs
    