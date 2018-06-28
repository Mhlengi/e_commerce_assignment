from django.contrib import admin
from core.models import Product, Store


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock',
                    'available', 'created_at']
    list_filter = ['available', 'created_at']
    list_editable = ['price', 'stock', 'available']


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


admin.site.register(Product, ProductAdmin)
admin.site.register(Store, StoreAdmin)
