from django.urls import path
from leads import views

app_name = 'leads'

urlpatterns = [
    path('new/', views.LeadCreateView.as_view(), name='create'),
    path('<int:pk>/', views.LeadDetailView.as_view(), name='detail'),
    path('', views.LeadListView.as_view(), name='list'),
    path('<int:pk>/edit/', views.LeadUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.LeadDeleteView.as_view(), name='delete'),
]
