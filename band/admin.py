from django.contrib import admin
from django.contrib.admin import ModelAdmin
from band.models import Band


class BandAdmin(ModelAdmin):
    list_display = ['name', 'genre']


admin.site.register(Band, BandAdmin)
