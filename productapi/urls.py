from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list_api, name='api_products'),
    path('', views.product_client_view, name='product_client'),
]