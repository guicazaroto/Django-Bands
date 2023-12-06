from django.contrib import admin
from django.contrib.admin import ModelAdmin
from shows.models import Show

class ShowAdmin(ModelAdmin):
    list_display = ['name', 'date', 'band', 'city']

admin.site.register(Show, ShowAdmin)