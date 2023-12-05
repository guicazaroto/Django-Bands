from django.contrib import admin
from django.urls import path
from band.views import home_band, edit_band, update_band

urlpatterns = [
    path('', home_band),
    path('<int:id>', edit_band, name='edit_band'),
    path('update/<int:id>', update_band, name='update_band'),
]
