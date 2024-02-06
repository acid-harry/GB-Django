from django.urls import path
from gb_aboutme import views
from django.contrib import admin

urlpatterns = [
    # Маршруты для админ панели
    path('admin/', admin.site.urls),

    # Маршруты для создания объектов
    path('create_client/', views.create_client, name='create_client'),
    path('create_product/', views.create_product, name='create_product'),
    path('create_order/', views.create_order, name='create_order'),
    
    # Маршруты для чтения объектов
    path('client/<int:client_id>/', views.get_client, name='get_client'),
    path('product/<int:product_id>/', views.get_product, name='get_product'),
    path('order/<int:order_id>/', views.get_order, name='get_order'),

    # Маршруты для обновления объектов
    path('update_client/<int:client_id>/', views.update_client, name='update_client'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('update_order/<int:order_id>/', views.update_order, name='update_order'),

    # Маршруты для удаления объектов
    path('delete_client/<int:client_id>/', views.delete_client, name='delete_client'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),

    # Маршруты для списка заказанных товаров за разные периоды времени
    path('ordered_products/<int:days>/', views.ordered_products, name='ordered_products'),
]