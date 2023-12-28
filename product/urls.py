from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_details/<slug:slug>', views.product_details, name='product_details'),
    path('search/', views.search, name='search'),
    path('category/<slug:slug>', views.product_list_by_category, name='product_list_by_category'),
]
