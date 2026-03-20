import random
from utils.faker_helpers import random_name, random_phone

def generate_medicos(num):
    medicos = []
    for i in range(1, num + 1):
        medicos.append({
            'IDMedico': i,
            'Nombre': random_name(),
            'Especialidad': random.choice(['MEDICO', 'BIOANALISTA']),
            'Password': 'hashed_password',
            'Telefono': random_phone(),
            'Rol': random.choice(['EMPLEADO', 'ADMIN']),
            'Correo': f"{random_name().replace(' ', '').lower()}@gmail.com",
            'ContrasenaTemporal': False
        })
    return medicos