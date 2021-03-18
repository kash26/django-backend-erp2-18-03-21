from django.urls import path

from . import views

urlpatterns = [
    path('order_list/', views.orderList, name="order_list"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),
]