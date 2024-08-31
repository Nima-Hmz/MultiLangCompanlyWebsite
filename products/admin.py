from django.contrib import admin

# Register your models here.

from .models import Category, Product

@admin.register(Category)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'en_name', 'slug')
    search_fields = ("title", "en_title", "slug")


@admin.register(Product)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'en_name', 'slug',  'available', 'position', 'category')
    search_fields = ("name", "en_name", "slug")
    list_filter = ("available",)