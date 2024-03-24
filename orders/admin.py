from django.contrib import admin

from orders.models import OrderModel


@admin.register(OrderModel)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'id_client', 'ip', 'comment', 'status', 'date']

    list_editable = ['phone', 'status', 'comment']

    readonly_fields = ('id_client', 'ip',)

    # Сортировка
    ordering = ['-date']

    list_per_page = 10

# admin.site.register(OrderModel, OrdersAdmin)
