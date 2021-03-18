from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register_shop/', views.registerShop, name="register_shop"),
    path('shop_list', views.shopList, name="shop_list"),
    path('update_shop/<str:pk>', views.updateShop, name="update_shop"),
]