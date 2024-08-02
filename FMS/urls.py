from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static #this is needed for file and image upload
from django.conf import settings
import fmsapp

# new imports
import cart
import shop
import orders


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('fmsapp.urls', namespace='fms') ),
    
    path ("orders/" , include('orders.urls' , namespace='order')),
    path ("shop/",include('shop.urls' , namespace='shop')),
    path ("cart/",include('cart.urls',namespace='cart')),
    path("blog/",include('blog.urls' , namespace='blog')),
    path("sales/",include('sales.urls' , namespace='sales')),
    # path('chapa-webhook', include('django_chapa.urls')),
    path('payment/',include('payment.urls' , namespace='payment'))
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)