from django.shortcuts import render
from .models import Order, Customer
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from .forms import CustomerProfileInfoForm, UserForm

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

class CustomerProfileCreateView(CreateView):
    
    def get(self, request, *args, **kwargs):
        context = {'user_form': UserForm(),'profile_form': CustomerProfileInfoForm()}
        return render(request, 'profiles/manage/profile/register.html', context)

    def post(self, request, *args, **kwargs):
        registered = False
        user_form = UserForm(data=request.POST)
        profile_form = CustomerProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
        return render(request, 'profiles/manage/profile/register.html',
                                {'user_form': user_form,
                                'profile_form': profile_form,
                                'registered':registered})
