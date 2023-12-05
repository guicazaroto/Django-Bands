from django.contrib import admin
from django.urls import path
from city.views import home_city, edit_city, update_city, add_city, save_city, delete_city

urlpatterns = [
    path('', home_city),
    path('<int:id>', edit_city, name='edit_city'),
    path('update/<int:id>', update_city, name='update_city'),
    path('add/', add_city, name='add_city'),
    path('save/', save_city, name='save_city'),
    path('delete/<int:id>', delete_city, name='delete_city')
]
