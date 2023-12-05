from django.contrib import admin
from django.urls import path
from band.views import home_band

urlpatterns = [
    path('', home_band)
]
