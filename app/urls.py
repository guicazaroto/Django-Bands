"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from shows_app.views import home_city, edit_city, update_city, add_city, save_city, delete_city
from shows_app.views import home_show, edit_show, update_show, add_show, save_show, delete_show, ApiShowsList, \
    home_band, \
    edit_band, update_band, add_band, save_band, delete_band

urlpatterns = [
    path('', RedirectView.as_view(url='/admin/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('shows/', home_show),
    path('shows/<int:id>', edit_show, name='edit_show'),
    path('shows/update/<int:id>', update_show, name='update_show'),
    path('shows/add/', add_show, name='add_show'),
    path('shows/save/', save_show, name='save_show'),
    path('shows/delete/<int:id>', delete_show, name='delete_show'),
    path('shows/api/', ApiShowsList.as_view()),

    # Bands Endpoints
    path('bands/', home_band),
    path('bands/<int:id>', edit_band, name='edit_band'),
    path('bands/update/<int:id>', update_band, name='update_band'),
    path('bands/add/', add_band, name='add_band'),
    path('bands/save/', save_band, name='save_band'),
    path('bands/delete/<int:id>', delete_band, name='delete_band'),

    # Cities Endpoints
    path('cities/', home_city),
    path('cities/<int:id>', edit_city, name='edit_city'),
    path('cities/update/<int:id>', update_city, name='update_city'),
    path('cities/add/', add_city, name='add_city'),
    path('cities/save/', save_city, name='save_city'),
    path('cities/delete/<int:id>', delete_city, name='delete_city')
]
