from django.contrib import admin

from .models import Flat, Abuse, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner','id')
    readonly_fields = ['created_at']
    list_display = ['address', 'price',
                    'new_building', 'construction_year', 'town','get_owners']
    list_editable = ['new_building']
    list_filter = ('new_building',)
    raw_id_fields = ("liked_by",)
    


@admin.register(Abuse)
class AbuseAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat",)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ("flats",)
    list_display = ['owner', 'owner_phone_pure', ]
   