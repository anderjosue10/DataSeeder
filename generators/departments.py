from datetime import timedelta
import random
from utils.faker_helpers import random_date

def generate_ordenes(num, clientes, medicos):
    ordenes = []
    for i in range(1, num + 1):
        fecha_orden = random_date()
        ordenes.append({
            'IDOrden': i,
            'IDCliente': random.choice(clientes)['IDCliente'],
            'IDMedico': random.choice(medicos)['IDMedico'],
            'FechaOrden': fecha_orden,
            'Estado': 'COMPLETADO',
            'fechaEntrega': fecha_orden + timedelta(days=random.randint(1,7)),
            'NumeroMuestra': random.randint(1,4)
        })
    return ordenes