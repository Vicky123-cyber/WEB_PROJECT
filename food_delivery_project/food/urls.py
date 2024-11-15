
from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('order/<int:food_id>/', views.place_order, name='place_order'),
    path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
]
