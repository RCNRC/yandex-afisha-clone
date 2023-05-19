from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import (
    SortableAdminMixin,
    SortableAdminBase,
    SortableStackedInline,
)
from .models import Place, Image


class MembershipInline(SortableStackedInline):
    model = Image
    extra = 0
    readonly_fields = ['preview_image']
    fields = ('serial_number', 'preview_image', 'content', 'place')

    def preview_image(self, image):
        max_height = 200
        return format_html(
            '<img src="{}" style="max-height:{}px" />',
            image.content.url,
            max_height,
        )


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ['title']
    inlines = [
        MembershipInline
    ]
