from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterationForm
from commerce_app.models import Stuff
from .models import Cart, CartItem, Order, OrderItem

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}.')
            return redirect('commerce_app-home')
    else:
        form = form = UserRegisterationForm()
    return render(request, 'users/register.html', context={'form': form})

@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)
    order_items = OrderItem.objects.filter(order__in=orders)

    context = {
        "orders" : orders,
        "order_items" : order_items,
    }
    return render(request, 'users/profile.html', context=context)

@login_required
def add_to_cart(request, item_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    item = get_object_or_404(Stuff, pk=item_id)

    cart_item, item_added = CartItem.objects.get_or_create(cart=cart, item=item)
    
    if not item_added:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f'1 more \"{item.name}\" added to your cart successfully.')
    
    else:
        messages.success(request, f'\"{item.name}\" added to your cart successfully.')
    
    return redirect("/")


def increase_quantity(request, item_id):
    cart = Cart.objects.get(user=request.user)
    item = get_object_or_404(CartItem, pk=item_id, cart=cart)
    item.quantity +=1
    item.save()
    return redirect("/cart/")


def decrease_quantity(request, item_id):
    cart = Cart.objects.get(user=request.user)
    item = get_object_or_404(CartItem, pk=item_id, cart=cart)

    if item.quantity > 1:
        item.quantity -=1
        item.save()
    elif item.quantity == 1:
        item.delete()

    return redirect("/cart/")


def remove_item(request, item_id):
    cart = Cart.objects.get(user=request.user)
    item = get_object_or_404(CartItem, pk=item_id, cart=cart)
    item.delete()
    return redirect("/cart/")