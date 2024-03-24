from django.contrib import admin

from data_site.modelMasters import MastersModel
from data_site.modelPrice import PriceModel
from data_site.modelsDataSite import DataSiteModel

admin.site.register(PriceModel)


@admin.register(DataSiteModel)
class MainAdmin(admin.ModelAdmin):
    list_display = ['brand_name', 'phone', 'instagram', 'address']

    list_editable = ['phone', 'instagram', 'address']


class MastersAdmin(admin.ModelAdmin):
    exclude = ('sort',)


admin.site.register(MastersModel, MastersAdmin)
