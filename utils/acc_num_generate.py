import random

def generate_account_number():
    prefix = f"BY{random.randint(10, 99)}OLMP"
    suffix = f"{random.randint(10**15, 10**16 - 1)}"
    return prefix + suffix