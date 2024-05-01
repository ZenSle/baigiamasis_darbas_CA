from django.contrib import admin
from . models import Category, Product


# admin.site.register(Category)
# admin.site.register(Product)

@admin.register(Category) # we want to make a prepopulated field
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product) # we want to make a prepopulated field
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
