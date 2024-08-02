from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category, Product as Sales
from cart.forms import CartAddProductForm
from cart.cart import Cart
class ProductListView(View):
    def get(self, request, category_slug=None):
        cart = Cart(request)
        category = None
        categories = Category.objects.all()
        products = Sales.objects.all()

        if category_slug:
            products = products.filter(slug=category_slug)

        return render(request, 'shop/product/list.html', {
            'category': category,
            'categories': categories,
            'products': products,
            'cart':cart
        })

class ProductDetailView(View):
    def get(self, request, id, slug):
        cart = Cart(request)
        product = get_object_or_404(Sales, id=id, slug=slug)
        cart_product_form = CartAddProductForm()
        return render(request, 'shop/product/detail.html', {
            'product': product,
            'cart_product_form': cart_product_form,
            'cart':cart
        })
