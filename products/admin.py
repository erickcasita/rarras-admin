from django.contrib import admin
from .models import  Categories, Brands, Products
# Register your models here.
class CategoriesAdmin (admin.ModelAdmin):
    readonly_fields = ("created",)
admin.site.register(Categories,CategoriesAdmin)
class BrandsAdmin (admin.ModelAdmin):
    readonly_fields = ("created",)
admin.site.register(Brands,BrandsAdmin)
class ProductsAdmin (admin.ModelAdmin):
    readonly_fields = ("created",)
admin.site.register(Products,ProductsAdmin)