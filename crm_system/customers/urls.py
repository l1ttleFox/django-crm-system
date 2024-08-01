from django.urls import path
from customers import views

app_name = 'customers'

urlpatterns = [
    path('new/', views.CustomerCreateView.as_view(), name='create'),
    path('<int:pk>/', views.CustomerDetailView.as_view(), name='detail'),
    path('', views.CustomerListView.as_view(), name='list'),
    path('<int:pk>/edit/', views.CustomerUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='delete'),
]
