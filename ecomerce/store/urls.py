from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.getItems, name='getItems'),
    path('addBook/', views.addBook, name='addBook'),
    path('addLaptop/', views.addLaptop, name='addLaptop'),
    path('addMobilePhone/', views.addMobilePhone, name='addMobilePhone'),
    path('addItem/<int:product_id>', views.addItem, name='addItem'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('updateBook/<int:product_id>', views.updateBook, name='updatebook')
]