from decimal import Decimal

from django.db import models, transaction

from apps.clients.models.models import Client
from utils.acc_num_generate import generate_account_number


class AcquiringContract(models.Model):
    contract_num = models.CharField(max_length=20, unique=True)
    acc_num = models.CharField(max_length=28, unique=True, default=generate_account_number)
    balance = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    commission = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.contract_num}'

class AcquiringTransactions(models.Model):
    date_transaction = models.DateTimeField(auto_now_add=True)
    sum_transaction = models.DecimalField(max_digits=12, decimal_places=2)
    num_card = models.CharField(max_length=20)
    sum_commission = models.DecimalField(max_digits=12, decimal_places=2)

    contract = models.ForeignKey(AcquiringContract, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        if is_new and not self.sum_commission:
            # Расчёт комиссии (например, 1.5%)
            self.sum_commission = round(self.sum_transaction * Decimal('0.015'), 2)

        with transaction.atomic():
            if is_new:
                self.contract.balance += self.sum_transaction
                self.contract.commission += self.sum_commission
                self.contract.save()
            super().save(*args, **kwargs)