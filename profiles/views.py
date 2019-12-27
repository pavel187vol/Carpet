from django.shortcuts import render
from .models import Order, Customer
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView

class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'orders/manage/order/order_list.html'

class OrderDetailView(DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'orders/manage/order/order_detail.html'

class OrderCreateView(CreateView):
    model = Order
    fields = ['title', 'text', 'image', 'price',
              'type_work']
    success_url = '/'
    template_name = 'orders/manage/order/order_create.html'

    def form_valid(self, form):
        # customer =
        form.instance.customer = Customer.objects.get(user=self.request.user)
        return super().form_valid(form)

class OrderDeleteView(DeleteView):
    model = Order
    success_url = '/'
    template_name = 'orders/manage/order/order_delete.html'
