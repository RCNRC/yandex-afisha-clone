from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image
from adminsortable2.admin import SortableAdminMixin, SortableAdminBase, SortableStackedInline, SortableTabularInline


class MembershipInline(SortableStackedInline):
    model = Image
    extra = 0
    readonly_fields = ["headshot_image"]
    fields = ("special_id", "headshot_image", "content", "place")

    def headshot_image(self, obj):
        max_heihght = 200
        max_width = int(obj.content.width / obj.content.height * 200)
        return format_html(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.content.url,
                width=obj.content.width
                if obj.content.width < max_width
                else max_width,
                height=obj.content.height
                if obj.content.height < max_heihght
                else max_heihght,
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
