from django.urls import path

from . import views
app_name = "sales"
urlpatterns = [
    
    path('login/', views.Login.as_view(), name='login'),
    path('login/', views.Logout.as_view(), name='logout'),
     #Sales Routes
   path("all/",views.SalesAll.as_view(), name="sales"),
   path("add/",views.SalesAdd.as_view(), name="create_sale"),
   path("<int:pk>/edit/",views.SalesUpdate.as_view(), name="edit_sale"),
   path("<int:pk>/delete/",views.DeleteSales.as_view(), name="delete_sale"),
   
    #orders
    path("orders/all/",views.OrdersAll.as_view(), name="orders"),
   
   
]
