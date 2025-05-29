from django.contrib import admin

from apps.acquiring.models import AcquiringContract, AcquiringTransactions


@admin.register(AcquiringContract)
class AcquiringContractAdmin(admin.ModelAdmin):
    list_display = ('contract_num', 'acc_num', 'balance', 'commission', 'created_at','is_active')
    search_fields = ['contract_num', 'acc_num', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at']

@admin.register(AcquiringTransactions)
class AcquiringTransactionsAdmin(admin.ModelAdmin):
    list_display = ('date_transaction', 'sum_transaction', 'num_card', 'sum_commission')
    search_fields = ['date_transaction', 'num_card',]
    list_filter = ['date_transaction']