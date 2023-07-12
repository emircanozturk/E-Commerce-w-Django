from users.models import Cart, CartItem


def total_quantity(request):
    if request.user.is_authenticated:
        cart , created= Cart.objects.get_or_create(user=request.user)
        items = CartItem.objects.filter(cart=cart)
        total_quantity = sum(item.quantity for item in items)
    else:
        total_quantity = 0

    context = {
        "total_quantity": total_quantity
    }
    
    return context