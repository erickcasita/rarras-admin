from django.contrib import admin
from .models import TypeMovement, WareHouses,  WareHouseConcept
# Register your models here.
class TypeMovementAdmin (admin.ModelAdmin):
    readonly_fields = ("created",)
admin.site.register(TypeMovement,TypeMovementAdmin)
class WareHouseAdmin (admin.ModelAdmin):
    readonly_fields = ("created",)
admin.site.register(WareHouses,WareHouseAdmin)
class WareHouseConceptAdmin (admin.ModelAdmin):
    readonly_fields = ("created",)
admin.site.register(WareHouseConcept,WareHouseConceptAdmin)