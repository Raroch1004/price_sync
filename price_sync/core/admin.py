from django.contrib import admin
from .models import Product, Site, PriceHistory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id',  'name']
    search_fields = ['name']

# admin.site.register(Product)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ['domain', 'name']
    search_fields = ['name']
    list_display_links = ['domain', 'name']

# admin.site.register(Site)


@admin.register(PriceHistory)
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'date', 'price']
    search_fields = ['product', 'date', 'price']
    list_display_links = ['id', 'product', 'date', 'price']

# admin.site.register(PriceHistory)
