from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, TemplateView
from products.models import Product
from ads.models import Advertisement
from leads.models import Lead
from customers.models import Customer


class UserLoginView(LoginView):
    """View для авторизации пользователя."""
    form_class = AuthenticationForm
    template_name = 'registration/login.html'


class IndexView(TemplateView):
    """View для главной страницы сайта с основной статистикой."""
    template_name = 'users/index.html'
    
    def get_context_data(self, **kwargs):
        context = {
            'products_count': Product.objects.all().count(),
            'advertisements_count': Advertisement.objects.all().count(),
            'leads_count': Lead.objects.all().count(),
            'customers_count': Customer.objects.all().count()
        }
        
        return context
    