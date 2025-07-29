from django.contrib import admin

from apps.credit.models import RequestCredit, CreditTransaction, CreditBalance, CreditContract

admin.site.register(RequestCredit)
admin.site.register(CreditContract)
admin.site.register(CreditBalance)
admin.site.register(CreditTransaction)
