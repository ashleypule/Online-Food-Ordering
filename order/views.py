from django.shortcuts import render, redirect

from cart.cart import Cart

from .models import Order, OrderItem

def start_order(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        first_name = request.POST.GET('first_name')
        last_name = request.POST.GET('last_name')
        email = request.POST.GET('email')
        address = request.POST.GET('address')
        phone = request.POST.GET('phone')

        order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name, email=email, address=address, phone=phone)

        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.price * quantity
            
            item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)
    
        return redirect('myaccount')
    return redirect('cart')     