from django.contrib import admin

from menu.models import Menu, Item


@admin.register(Item)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent',]
    list_filter = ['parent',]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title',]