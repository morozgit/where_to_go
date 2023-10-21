from adminsortable2.admin import (SortableAdminBase, SortableAdminMixin,
                                  SortableTabularInline)
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, PlaceImage


@admin.register(PlaceImage)
class PlaceImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('place',)
    autocomplete_fields = ['place']


class PlaceImageInline(SortableTabularInline, admin.TabularInline):
    model = PlaceImage
    readonly_fields = ('get_preview',)

    def get_preview(self, image):
        return format_html('<img src="{}" style="max-height: 200px; max-width: auto;" />', image.image.url,)



@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = (
        'title',
        )
    search_fields = ['title']
    inlines = [
        PlaceImageInline,
    ]