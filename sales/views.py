from django.shortcuts import render , redirect , resolve_url
from django.views.generic import CreateView,ListView,UpdateView,View , TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from shop.models import Product as Sales
from fmsapp.forms import SalesForm , LoginForm
from django.utils.text import slugify


from orders.models import Order

#This is the view used for desplaying the ordered lists


class OrdersAll(LoginRequiredMixin,ListView):
    login_url = 'fms:login'
    model = Order
    template_name = 'sales/orders/index.html'
    context_object_name = 'orders'


class Login(LoginView):
    template_name = 'sales/home/login.html'
    form_class = LoginForm
    model = get_user_model()
    def get_success_url(self):
        query = get_user_model().objects.get(pk=self.request.user.pk)
        self.request.session['username'] = query.username
        #self.request.session['']
        url = resolve_url('sales:sales')
        return url

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('sales:login', permanent=True)

# Sales All
# class SalesAdd(LoginRequiredMixin,CreateView):
#     model = Sales 
#     login_url = 'sales:login'
#     form_class = SalesForm
#     template_name = 'sales/sales/create.html'
#     success_url = reverse_lazy('sales:sales')

class SalesAdd(LoginRequiredMixin, CreateView):
    model = Sales 
    login_url = 'sales:login'
    form_class = SalesForm
    template_name = 'sales/sales/create.html'
    success_url = reverse_lazy('sales:sales')

    def form_valid(self, form):
        sales = form.save(commit=False)
        sales.slug = slugify(sales.name)
        sales.save()
        return super().form_valid(form)


class SalesAll(LoginRequiredMixin,ListView):
    login_url = 'sales:login'
    model = Sales
    template_name = 'sales/sales/index.html'
    context_object_name = 'sales'

class SalesUpdate (LoginRequiredMixin,UpdateView):
    model = Sales
    login_url = 'sales:login'
    form_class = SalesForm
    template_name = 'sales/sales/edit.html'
    success_url = reverse_lazy ('sales:sales')

class DeleteSales(LoginRequiredMixin,View):
    login_url = 'sales:login'

    def get(self, request,pk):
        sale = Sales.objects.get(pk=pk)
        sale.delete()
        return redirect('sales:sales')