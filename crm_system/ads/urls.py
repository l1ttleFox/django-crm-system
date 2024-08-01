from django.urls import path
from ads import views

app_name = 'ads'

urlpatterns = [
    path('new/', views.AdvertisementCreateView.as_view(), name='create'),
    path('<int:pk>/', views.AdvertisementDetailView.as_view(), name='detail'),
    path('', views.AdvertisementListView.as_view(), name='list'),
    path('<int:pk>/edit/', views.AdvertisementUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.AdvertisementDeleteView.as_view(), name='delete'),
    path('statistic/', views.AdvertisementStatisticView.as_view(), name='statistic'),
]
