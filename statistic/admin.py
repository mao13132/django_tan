from django.contrib import admin

from statistic.models import ClickersModule


@admin.register(ClickersModule)
class ClickersAdmin(admin.ModelAdmin):
    list_display = ['id', 'utm', 'user_agent', 'ip', 'session_id', 'date']

    readonly_fields = ('id', 'utm', 'ip', 'session_id', 'date', 'user_agent', 'computer_name', 'processor_info')

    ordering = ['-date']
