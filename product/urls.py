from django.urls import path

from . import views

urlpatterns = [
    path('product_list/', views.productList, name="product_list"),
    path('create_product/', views.createProduct, name="create_product"),
    path('update_product/<str:pk>', views.updateProduct, name="update_product"),
    path('delete_product/<str:pk>', views.deleteProduct, name="delete_product"),
]
