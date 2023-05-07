from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image
from adminsortable2.admin import SortableAdminMixin, SortableAdminBase, SortableStackedInline, SortableTabularInline


class MembershipInline(SortableStackedInline):
    model = Image
    extra = 0
    readonly_fields = ["headshot_image"]
    fields = ("serial_number", "headshot_image", "content", "place")

    def headshot_image(self, obj):
        max_heihght = 200
        return format_html(
            '<img src="{url}" style="max-height:{height}px" />'.format(
                url=obj.content.url,
                height=max_heihght,
            )
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
