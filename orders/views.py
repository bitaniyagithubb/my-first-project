from django.shortcuts import render , redirect , reverse
from django.views import View
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
# from .tasks import order_created

# class OrderCreateView(View):
#     def get(self, request):
#         cart = Cart(request)
#         form = OrderCreateForm
#         return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

#     def post(self, request):
#         cart = Cart(request)
#         form = OrderCreateForm(request.POST)

#         if form.is_valid():
#             order = form.save()

#             for item in cart:
#                 OrderItem.objects.create(
#                     order=order,
#                     product=item['product'],
#                     price=item['price'],
#                     quantity=item['quantity']
#                 )

#             cart.clear()
#             return render(request, 'orders/order/created.html', {'order': order})

#         return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})
