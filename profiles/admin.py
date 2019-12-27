from django.contrib import admin
from .models import Customer, Executer,\
                    Order, TypeWork, DescriptionOrder

@admin.register(Customer)
class CumstomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone',
                    'email', 'order']
    list_filter = ['order', 'first_name']
    search_fields = ['first_name', 'last_name', 'order'
                     'phone', 'email']

@admin.register(Executer)
class ExecuterAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone',
                    'email']
    list_filter = ['first_name']
    search_fields = ['first_name', 'last_name', 'description'
                     'phone', 'email']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'executor', 'condition']
    list_filter = ['condition']
    search_fields = ['customer', 'executor']

@admin.register(TypeWork)
class TypeWorkAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

@admin.register(DescriptionOrder)
class DescriptionOrderAdmin(admin.ModelAdmin):
    list_display = ['order', 'type_work', 'price']
    list_filter = ['price']
    search_fields = ['type_work', 'price']
