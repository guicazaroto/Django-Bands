from django.contrib import admin
from django.urls import path
from shows.views import home_show, edit_show, delete_show, add_show, save_show, update_show, ApiShowsList

urlpatterns = [
    path('', home_show),
    path('/<int:id>', edit_show, name='edit_show'),
    path('/update/<int:id>', update_show, name='update_show'),
    path('/add', add_show, name='add_show'),
    path('/save', save_show, name='save_show'),
    path('/delete/<int:id>', delete_show, name='delete_show'),
    path('/api', ApiShowsList.as_view()),
]
