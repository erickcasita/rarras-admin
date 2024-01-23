from django.contrib import admin
from .models import Store
# Register your models here.
class StoreAdmin (admin.ModelAdmin):
    readonly_fields = ("created",)
admin.site.register(Store,StoreAdmin)