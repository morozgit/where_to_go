from django.contrib import admin
from .models import Place, PlaceImage


# @admin.register(PlaceImage)
class PlaceImageAdmin(admin.TabularInline):
    # list_display = (
    #     'combined_fields',
    #     )
    
    # def combined_fields(self, obj):
    #     return f"{obj.pk} {obj.place}"
    model = PlaceImage


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        )
    search_fields = ['title']
    inlines = [
        PlaceImageAdmin,
    ]

