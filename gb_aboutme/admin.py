from django.contrib import admin
from .models import Client, Product, Order

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'photo')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'total_amount', 'order_date')

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)