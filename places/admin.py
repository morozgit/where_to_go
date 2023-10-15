from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.html import format_html


# @admin.register(PlaceImage)
class PlaceImageAdmin(admin.TabularInline):
    model = PlaceImage
    readonly_fields = ("place_image",)

    def place_image(self, obj):
        return format_html('<img src="{}" height=200 />', obj.image.url,)



@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        )
    search_fields = ['title']
    inlines = [
        PlaceImageAdmin,
    ]