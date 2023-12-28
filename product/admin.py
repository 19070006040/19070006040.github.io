from django.contrib import admin
from . import models


# Register your models here.

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["category_name", "slug"]
    search_fields = ["category_name"]
    readonly_fields = ["slug"]


admin.site.register(models.Category, CategoryModelAdmin)


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["product_name", "slug"]
    search_fields = ["product_name"]
    readonly_fields = ["slug"]


admin.site.register(models.Product, ProductModelAdmin)
