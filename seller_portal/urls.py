from django.urls import path

from . import views

urlpatterns = [
    path('seller_login/', views.sellerLoginPage, name='seller_login'),
    path('seller_portal_list/', views.orderList, name="seller_portal_list"),
    path('register_portal_seller/<str:pk>', views.createOrder, name="create_order"),
    path('update_portal_seller/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_portal_seller/<str:pk>', views.deleteOrder, name="delete_order"),
]