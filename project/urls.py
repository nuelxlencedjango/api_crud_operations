from django.urls import path
from .views import *
from .import views

app_name = 'project'


urlpatterns = [
 
    path('', views.apiOverView, name='home'),
    path('product_list/', views.showProducts, name='product_list'),
    path('product_detail/<int:pk>/', views.productDetail, name='product_detail'),
    path('product_create/', views.createProduct, name='product_create'),
    path('product_update/<int:pk>/', views.productUpdate, name='product_update'),
    path('product_delete/<int:pk>/', views.deleteProduct, name='product_delete'),
  
]



