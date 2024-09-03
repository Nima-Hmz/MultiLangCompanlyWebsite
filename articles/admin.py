from django.contrib import admin

# Register your models here.

from .models import Article, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'entitle', 'slug', 'category', 'pub_date', 'status')
    search_fields = ("title", "entitle", "slug")
    list_filter = ("status",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'entitle', 'slug')
    search_fields = ("title", "entitle", "slug")