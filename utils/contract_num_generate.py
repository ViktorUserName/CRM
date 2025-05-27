import random
from datetime import date


def generate_contract_number():
    prefix = f"{date.today()}-"
    suffix = f"{random.randint(10 ** 8, 10 ** 9 - 1)}"
    contract_num = prefix + suffix
    return contract_num
