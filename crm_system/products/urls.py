from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('new/', views.ProductCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('', views.ProductListView.as_view(), name='list'),
    path('<int:pk>/edit/', views.ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete'),
]
