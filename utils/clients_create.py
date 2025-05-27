from apps.clients.models.models import Client, LegalDetails, IndividualDetails
from django.db import transaction

def create_client(data: dict) -> Client:
    """
    Создаёт клиента и соответствующие детали (юр/физ) в одной транзакции.
    """
    with transaction.atomic():
        is_legal = data.get("is_legal")

        client = Client.objects.create(
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            is_legal=is_legal
        )

        if is_legal:
            LegalDetails.objects.create(
                client=client,
                inn=data["inn"],
                kpp=data["kpp"],
                ogrn=data["ogrn"],
                address=data["address"]
            )
        else:
            IndividualDetails.objects.create(
                client=client,
                passport_number=data["passport_number"],
                birth_date=data["birth_date"]
            )

    return client
