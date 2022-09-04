from django.contrib import admin

from .models import Category, Product

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "is_available", "time_created"]
    list_editable = ["price", "is_available"]
    list_filter = ["is_available", "time_created"]
    prepopulated_fields = {"slug": ("name",)}
