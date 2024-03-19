from django.contrib import admin

from orders.models import OrderModel


class OrdersAdmin(admin.ModelAdmin):
    readonly_fields = ('id_client',)


admin.site.register(OrderModel, OrdersAdmin)
