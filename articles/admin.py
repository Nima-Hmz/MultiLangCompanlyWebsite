from django.contrib import admin

# Register your models here.

from .models import Article, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'en_title', 'slug', 'category', 'pub_date', 'status')
    search_fields = ("title", "en_title", "slug")
    list_filter = ("status",)


@admin.register(Category)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'en_title', 'slug',  'created')
    search_fields = ("title", "en_title", "slug")