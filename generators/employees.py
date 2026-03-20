import random
from datetime import datetime, timedelta
from utils.faker_helpers import random_name, random_date, random_phone

def generate_clientes(num):
    clientes = []
    for i in range(1, num + 1):
        clientes.append({
            'IDCliente': i,
            'Nombre': random_name(),
            'FechaNacimiento': random_date(),
            'Genero': random.choice(['M', 'F']),
            'Telefono': random_phone()
        })
    return clientes