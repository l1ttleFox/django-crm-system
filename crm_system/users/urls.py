from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('users/login/', views.UserLoginView.as_view(), name='login'),
    path('', views.IndexView.as_view(), name='index'),
]
