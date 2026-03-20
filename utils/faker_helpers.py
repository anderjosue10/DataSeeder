import random
from datetime import datetime, timedelta

nombres = ['Juan Pérez', 'María García', 'Carlos López', 'Ana Martínez', 'Pedro Sánchez', 'Laura Díaz', 'José Rodríguez', 'Carmen Fernández', 'Miguel González', 'Isabel Jiménez']

def random_name():
    return random.choice(nombres)

def random_date():
    start = datetime(2000, 1, 1)
    end = datetime(2023, 12, 31)
    return start + timedelta(days=random.randint(0, (end - start).days))

def random_phone():
    return f"{random.randint(10000000, 99999999)}"