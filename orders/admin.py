from django.contrib import admin

from orders.models import OrderModel


@admin.register(OrderModel)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'id_client', 'comment', 'date']

    list_editable = ['phone', 'comment']

    readonly_fields = ('id_client',)

    # Сортировка
    ordering = ['-date']

    list_per_page = 10

# admin.site.register(OrderModel, OrdersAdmin)
