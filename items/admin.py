from django.contrib import admin
from .models import Item 
# Register your models here.

# admin.site.register(Item)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')#admin panelda ko'rsatiladigan ustusenlar
    search_fields =['name'] # admin panel search field yaratish