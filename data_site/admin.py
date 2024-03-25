from django.contrib import admin
from django.utils.safestring import mark_safe

from data_site.modelMasters import MastersModel
from data_site.modelPrice import PriceModel
from data_site.modelsDataSite import DataSiteModel


@admin.register(PriceModel)
class MainAdmin(admin.ModelAdmin):
    list_display = ['description', 'name', 'price']

    list_editable = ['name', 'price']


@admin.register(MastersModel)
class MainAdmin(admin.ModelAdmin):
    list_display = ['get_html_photo', 'name', 'post', 'description']

    list_editable = ['name', 'post']

    def get_html_photo(self, obj):
        if obj.avatar:
            return mark_safe(f"<img src='{obj.avatar.url}' width=50>")

    get_html_photo.short_description = f'Фото'


class MastersAdmin(admin.ModelAdmin):
    exclude = ('sort',)


admin.site.register(DataSiteModel)
