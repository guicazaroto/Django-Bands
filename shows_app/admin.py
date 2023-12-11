from django.contrib import admin
from django.contrib.admin import ModelAdmin
from shows_app.models import Band, City


class BandAdmin(ModelAdmin):
    list_display = ['name', 'genre']


class CityAdmin(ModelAdmin):
    list_display = ['name', 'state']


admin.site.register(City, CityAdmin)
admin.site.register(Band, BandAdmin)
