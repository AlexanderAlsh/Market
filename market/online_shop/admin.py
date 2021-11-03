from django.contrib import admin
from .models import *


class SmartphonesAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'price', 'image', 'diag', 'SIM']


class TelevisionAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'price', 'image', 'diag']


class CleanerAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'price', 'image']


class DefrostAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'price', 'image']


class WashingAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'price', 'image']


class FridgeAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'price', 'image']


class CatalogAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'image']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'url', 'image']


admin.site.register(Smartphones, SmartphonesAdmin)
admin.site.register(Television, TelevisionAdmin)
admin.site.register(Cleaner, CleanerAdmin)
admin.site.register(Defrost, DefrostAdmin)
admin.site.register(Washing, WashingAdmin)
admin.site.register(Fridge, FridgeAdmin)
admin.site.register(Slider, SliderAdmin)