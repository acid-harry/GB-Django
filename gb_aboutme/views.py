import logging
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Client, Product, Order
from django.utils import timezone
from datetime import timedelta

# Получаем объект логгера для этого модуля
logger = logging.getLogger(__name__)

# Create
def create_client(request):
    if request.method == 'POST':
        # Получение данных из POST-запроса
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        # Создание клиента
        client = Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)
        # Логируем создание клиента
        logger.info(f'Создан клиент: {client.name}')
        return HttpResponse(f'Клиент {client.name} успешно создан.')
    else:
        return HttpResponse('Неверный метод запроса.')

def create_product(request):
    # Аналогично функции create_client, но для создания продукта
    pass

def create_order(request):
    # Аналогично функции create_client, но для создания заказа
    pass

# Read
def get_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    # Логируем получение клиента
    logger.info(f'Получен клиент: {client.name}')
    return HttpResponse(f'Клиент: {client.name}, Email: {client.email}, Телефон: {client.phone_number}, Адрес: {client.address}')

def get_product(request, product_id):
    # Аналогично функции get_client, но для получения продукта
    pass

def get_order(request, order_id):
    # Аналогично функции get_client, но для получения заказа
    pass

# Update
def update_client(request, client_id):
    if request.method == 'POST':
        client = get_object_or_404(Client, pk=client_id)
        # Обновление данных клиента
        client.name = request.POST.get('name')
        client.email = request.POST.get('email')
        client.phone_number = request.POST.get('phone_number')
        client.address = request.POST.get('address')
        client.save()
        # Логируем обновление клиента
        logger.info(f'Обновлен клиент: {client.name}')
        return HttpResponse(f'Клиент {client.name} успешно обновлен.')
    else:
        return HttpResponse('Неверный метод запроса.')

def update_product(request, product_id):
    # Аналогично функции update_client, но для обновления продукта
    pass

def update_order(request, order_id):
    # Аналогично функции update_client, но для обновления заказа
    pass

# Delete
def delete_client(request, client_id):
    if request.method == 'POST':
        client = get_object_or_404(Client, pk=client_id)
        client.delete()
        # Логируем удаление клиента
        logger.info(f'Удален клиент: {client.name}')
        return HttpResponse('Клиент успешно удален.')
    else:
        return HttpResponse('Неверный метод запроса.')

def delete_product(request, product_id):
    # Аналогично функции delete_client, но для удаления продукта
    pass

def delete_order(request, order_id):
    # Аналогично функции delete_client, но для удаления заказа
    pass

def ordered_products(request, days):
    end_date = timezone.now()
    start_date = end_date - timedelta(days=days)
    
    # Получаем все заказы за указанный период
    orders = Order.objects.filter(order_date__range=(start_date, end_date))
    
    # Собираем все товары из этих заказов в один список
    ordered_products = []
    for order in orders:
        ordered_products.extend(order.products.all())
    
    # Убираем дубликаты товаров
    unique_products = set(ordered_products)
    
    context = {
        'products': unique_products,
        'period': days
    }
    
    return render(request, 'ordered_products.html', context)