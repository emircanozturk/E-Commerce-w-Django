from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from commerce_app.models import Stuff
from users.models import Cart, CartItem, Order, OrderItem

# Create your views here.

def home(request):
    context = {
        "stuffs" : Stuff.objects.all(),
    }
    return render(request, "commerce_app/home.html", context=context)


def about(request):
    return render(request, "commerce_app/about.html")


def filter_by_category(request, category):
    filtered_stuffs = Stuff.objects.filter(category=category)
    context = {
        "filtered_stuffs" : filtered_stuffs,
        "category" : category,
    }
    return render(request, "commerce_app/category.html", context=context)


@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user = request.user)
    cart_items = CartItem.objects.filter(cart = cart)
    total_price = sum(item.total_price() for item in cart_items)
    context = {
        "cart" : cart,
        "cart_items" : cart_items,
        "total_price" : total_price,
    }
    return render(request, "commerce_app/cart.html", context=context)


@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user = request.user)
    cart_items = CartItem.objects.filter(cart = cart)
    total_price = sum(item.total_price() for item in cart_items)

    if request.method == "POST":
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        phone_number = request.POST["phonenumber"]
        address = request.POST["address"]
        country = request.POST["country"]
        state = request.POST["state"]
        zip_code = request.POST["zipcode"]

        order = Order(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            country=country,
            state=state,
            zip_code=zip_code,
            email=request.user.email,
            user=request.user,
        )

        order.save()

        for cart_item in cart_items:
            order_item = OrderItem(
                order=order,
                item=cart_item.item,
                quantity=cart_item.quantity,
            )
            order_item.save()

        cart_items.delete()

        return redirect("/profile/")

    else:
        return render(request, "commerce_app/checkout.html")