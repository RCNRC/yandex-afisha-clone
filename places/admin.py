from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


class MembershipInline(admin.TabularInline):
    model = Image
    readonly_fields = ["headshot_image"]
    fields = ("special_id", "headshot_image", "content", "place")

    def headshot_image(self, obj):
        max_heihght = 200
        max_width = 200
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
    

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline
    ]
