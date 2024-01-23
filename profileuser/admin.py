from django.contrib import admin
from .models import TypeUser, ProfileUser
# Register your models here.
class TypeUserAdmin (admin.ModelAdmin):
    readonly_fields = ("created",)
admin.site.register(TypeUser,TypeUserAdmin)
class ProfileUserAdmin (admin.ModelAdmin):
    readonly_fields = ("created",)
admin.site.register(ProfileUser,ProfileUserAdmin)