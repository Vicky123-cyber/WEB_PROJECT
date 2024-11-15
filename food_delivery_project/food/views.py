from django.shortcuts import render, redirect
from .models import FoodItem, Order
from django.http import HttpResponse

# Create your views here.

#View for displaying the menu
def menu(request):
    foods = FoodItem.objects.all()
    return render(request,'food/menu.html',{'foods':foods})

#View for submitting an order
def place_order(request, food_id):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        quantity = int(request.POST['quantity'])
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        food_item = FoodItem.objects.get(id=food_id)
        order = Order(customer_name=customer_name, food_item=food_item, quantity=quantity, address=address, phone_number=phone_number)
        order.save()
        return redirect('order_configuration',order_id=order_id)  # type: ignore

#View for order confirmation
def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'food/order_confirmation.html', {'order':order})
        


