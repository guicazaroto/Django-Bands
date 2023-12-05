from django.contrib import admin
from django.urls import path
from band.views import home_band, edit_band, update_band, add_band, save_band, delete_band

urlpatterns = [
    path('', home_band),
    path('<int:id>', edit_band, name='edit_band'),
    path('update/<int:id>', update_band, name='update_band'),
    path('add/', add_band, name='add_band'),
    path('save/', save_band, name='save_band'),
    path('delete/<int:id>', delete_band, name='delete_band')
]
