from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('flat', 'owner')


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owners__name')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable  = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = [
        OwnerInline,
    ]


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['user', 'flat', 'text']
    search_fields = ['text', 'user__username', 'flat__address']
    raw_id_fields = ('flat', 'user')


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phonenumber', 'pure_phonenumber')
    raw_id_fields = ('flats',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)