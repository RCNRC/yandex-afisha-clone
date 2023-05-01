from django.contrib import admin
from .models import Place, Image


class MembershipInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline
    ]


admin.site.register(Image)
