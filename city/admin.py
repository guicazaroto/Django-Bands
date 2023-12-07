from django.contrib import admin
from django.contrib.admin import ModelAdmin
from city.models import City


class CityAdmin(ModelAdmin):
    list_display = ['name', 'state']


admin.site.register(City, CityAdmin)
