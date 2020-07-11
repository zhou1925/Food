from django.urls import path
from . import views

app_name='food'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('edit/', views.edit_account2, name='edit-account'),
    path('meal/', views.restaurant_meal, name='restaurant-meal'),
    path('orders/', views.restaurant_order, name='restaurant-order'),
    path('report/', views.restaurant_report, name='restaurant-report'),
    path('add_meal/', views.add_meal, name='add-meal'),
    path('edit_meal/<int:meal_id>/', views.edit_meal, name='edit-meal'),
    
]
