from django.db import models
from django.db.models import ForeignKey, OneToOneField

from apps.clients.models.models import Client
from utils.contract_num_generate import generate_contract_number


class RequestCredit(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        APPROVED = 'Approved'
        CANCELLED = 'Canceled'

    client = ForeignKey(Client, on_delete=models.CASCADE, related_name='request_credits')
    amount_request = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    term_months = models.IntegerField()
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
    )



class CreditContract(models.Model):
    class StatusChoices(models.TextChoices):
        ACTIVE = 'Active'
        PAID_OFF = 'Paid Off'

    request_credit = models.OneToOneField(RequestCredit, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='credit_contract')
    amount = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    contract_number = models.CharField(max_length=28, unique=True, default=generate_contract_number)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    loan_term = models.IntegerField(default=0)

    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.ACTIVE,
    )



class CreditBalance(models.Model):
    contract = OneToOneField(CreditContract, on_delete=models.CASCADE)
    current_balance = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    last_update = models.DateTimeField(auto_now=True)


class CreditTransaction(models.Model):
    balance = ForeignKey(CreditBalance, on_delete=models.CASCADE, related_name='credit_transactions')
    amount = models.DecimalField(decimal_places=2, max_digits=15, default=0)
    transaction_date = models.DateTimeField(auto_now_add=True)

