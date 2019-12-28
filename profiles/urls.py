from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('order/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('order/delete/<int:pk>', views.OrderDeleteView.as_view(), name='order_delete'),
    path('profile/register_customer/', views.CustomerProfileCreateView.as_view(), name='register_customer'),
    path('profile/register_executer/', views.ExecuterProfileCreateView.as_view(), name='register_executer'),
]
