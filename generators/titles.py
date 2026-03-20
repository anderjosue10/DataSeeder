import random

tipo_examenes = [
    {'IDTipoExamen': 1, 'NombreExamen': 'SEROLOGÍA', 'Precio': 200.00},
    {'IDTipoExamen': 2, 'NombreExamen': 'HEMATOLOGÍA', 'Precio': 200.00},
    {'IDTipoExamen': 3, 'NombreExamen': 'UROANALISIS', 'Precio': 200.00},
    {'IDTipoExamen': 4, 'NombreExamen': 'QUÍMICA SANGUÍNEA', 'Precio': 0.00},
    {'IDTipoExamen': 5, 'NombreExamen': 'EXÁMENES DIVERSOS', 'Precio': 0.00},
    {'IDTipoExamen': 6, 'NombreExamen': 'PARASITOLOGÍA', 'Precio': 200.00},
    {'IDTipoExamen': 10, 'NombreExamen': 'CITOLOGÍA FECAL', 'Precio': 100.00},
    {'IDTipoExamen': 11, 'NombreExamen': 'COAGULACIÓN', 'Precio': 200.00},
    {'IDTipoExamen': 12, 'NombreExamen': 'UROCULTIVO', 'Precio': 200.00},
    {'IDTipoExamen': 13, 'NombreExamen': 'UROCULTIVO NEGATIVO', 'Precio': 200.00}
]

muestras = [
    {'id': 1, 'Muestra': 'HECES'},
    {'id': 2, 'Muestra': 'SANGRE'},
    {'id': 3, 'Muestra': 'SUERO'},
    {'id': 4, 'Muestra': 'ORINA'}
]

def generate_detalle_ordenes(num, ordenes):
    detalles = []
    id_det = 1
    for orden in ordenes:
        num_det = random.randint(1,3)
        for _ in range(num_det):
            detalles.append({
                'IDDetalleOrden': id_det,
                'IDOrden': orden['IDOrden'],
                'IDTipoExamen': random.choice(tipo_examenes)['IDTipoExamen'],
                'IDMuestra': random.choice(muestras)['id']
            })
            id_det += 1
    return detalles