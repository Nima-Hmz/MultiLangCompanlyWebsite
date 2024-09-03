from django.contrib import admin

# Register your models here.

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'enname', 'slug', 'star')
    search_fields = ("name", "enname", "slug")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'enname', 'slug',  'available', 'position', 'pub_date')
    search_fields = ("name", "enname", "slug")
    list_filter = ("available",)