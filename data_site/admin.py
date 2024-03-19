from django.contrib import admin

from data_site.modelPrice import PriceModel
from data_site.modelsDataSite import DataSiteModel

admin.site.register(DataSiteModel)
admin.site.register(PriceModel)
