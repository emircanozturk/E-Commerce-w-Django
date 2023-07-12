from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="commerce_app-home"),
    path('about/', views.about, name="commerce_app-about"),
    path('cart/', views.cart, name="commerce_app-cart"),
    path('category/<str:category>/', views.filter_by_category, name="commerce_app-filterbycategory"),
    path('checkout/', views.checkout, name="commerce_app-checkout"),
]
