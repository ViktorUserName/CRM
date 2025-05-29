from django.contrib import admin

from apps.acquiring.models import AcquiringContract


@admin.register(AcquiringContract)
class AcquiringContractAdmin(admin.ModelAdmin):
    list_display = ('contract_num', 'acc_num', 'balance', 'commission', 'created_at','is_active')
    search_fields = ['contract_num', 'acc_num', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at']

