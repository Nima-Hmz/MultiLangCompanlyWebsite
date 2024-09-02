from django.contrib import admin

# Register your models here.

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'en_name', 'slug')
    search_fields = ("title", "en_title", "slug")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'en_name', 'slug',  'available', 'position', 'pub_date')
    search_fields = ("name", "en_name", "slug")
    list_filter = ("available",)