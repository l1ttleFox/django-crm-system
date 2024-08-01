from django.urls import path
from contracts import views

app_name = 'contracts'

urlpatterns = [
    path('new/', views.ContractCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ContractDetailView.as_view(), name='detail'),
    path('', views.ContractListView.as_view(), name='list'),
    path('<int:pk>/edit/', views.ContractUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.ContractDeleteView.as_view(), name='delete'),
]
