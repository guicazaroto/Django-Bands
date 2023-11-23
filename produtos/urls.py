from django.contrib import admin
from django.urls import path
from .views import home, add, save, edit, update, delete

urlpatterns = [
    path('', home),
    path('add/', add, name='add'),
    path('save/', save, name='save'),
    path('<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete')
]
