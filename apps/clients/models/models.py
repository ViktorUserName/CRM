from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    is_legal = models.BooleanField()

    def __str__(self):
        type_label = "Юр. лицо" if self.is_legal else "Физ. лицо"
        return f"{type_label} — {self.name} {self.surname}"


class LegalDetails(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    inn = models.CharField(max_length=12, unique=True, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    ogrn = models.CharField(max_length=13, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"ИНН: {self.inn} | {self.client.name} {self.client.surname}"


class IndividualDetails(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    unp = models.CharField(max_length=18, unique=True, blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"УНП: {self.unp} | {self.client.name} {self.client.surname}"