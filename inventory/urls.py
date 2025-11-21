from . import views
from django.urls import path



urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('add/', views.add_product, name='add-product'),
    path('delete/<int:id>/', views.delete_product, name='delete-product'),
    path('update/<int:id>/', views.update_stock, name='update-stock'),
]
