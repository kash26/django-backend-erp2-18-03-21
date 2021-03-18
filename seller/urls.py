from django.urls import path

from . import views

urlpatterns = [
    path('seller_list/', views.sellerList, name="seller_list"),
    path('register_seller/', views.registerSeller, name="register_seller"),
    path('update_seller/<str:pk>', views.updateSeller, name="update_seller"),
    path('delete_seller/<str:pk>', views.deleteSeller, name="delete_seller"),
]
