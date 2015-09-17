from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    fields = ['name', 'phone', 'text']

admin.site.register(Item, ItemAdmin)
