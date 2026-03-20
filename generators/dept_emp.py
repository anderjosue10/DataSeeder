from datetime import timedelta
import random
from utils.faker_helpers import random_date

parametros = [
    {'IDParametro': 1, 'IDTipoExamen': 1, 'NombreParametro': 'Proteína C Reactiva (PCR)', 'Precio': 100.00},
    {'IDParametro': 4, 'IDTipoExamen': 2, 'NombreParametro': 'Eritrocitos', 'Precio': 15.00},
    {'IDParametro': 18, 'IDTipoExamen': 3, 'NombreParametro': 'Color', 'Precio': 25.00},
]

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

def generate_facturas(num, clientes, medicos, ordenes):
    facturas = []
    for i in range(1, num + 1):
        orden = random.choice(ordenes)
        fecha_fact = orden['FechaOrden'] + timedelta(days=random.randint(1,10))
        facturas.append({
            'IDFactura': i,
            'IDCliente': orden['IDCliente'],
            'FechaFactura': fecha_fact,
            'Total': round(random.uniform(100, 1000), 2),
            'IDMedico': orden['IDMedico'],
            'TipoFacturacion': random.choice(['EXAMEN', 'PARAMETRO'])
        })
    return facturas

def generate_detalle_facturas(facturas, detalles_orden):
    detalles_fact = []
    id_det_fact = 1
    for factura in facturas:
        num_det = random.randint(1,3)
        for _ in range(num_det):
            detalles_fact.append({
                'IDDetalleFactura': id_det_fact,
                'IDFactura': factura['IDFactura'],
                'IDDetalleOrden': random.choice(detalles_orden)['IDDetalleOrden'],
                'Subtotal': round(random.uniform(50, 500), 2),
                'Precio': round(random.uniform(50, 500), 2),
                'NombreParametro': random.choice(['UROANALISIS', 'HEMATOLOGÍA', 'SEROLOGÍA']),
                'Idparametro': random.choice(parametros)['IDParametro'],
                'IdtipoExamen': random.choice(tipo_examenes)['IDTipoExamen']
            })
            id_det_fact += 1
    return detalles_fact

def generate_resultados(detalles_orden, parametros):
    resultados = []
    id_res = 1
    for det in detalles_orden:
        num_res = random.randint(1,5)
        for _ in range(num_res):
            param = random.choice(parametros)
            resultados.append({
                'IDResultado': id_res,
                'IDDetalleOrden': det['IDDetalleOrden'],
                'IDParametro': param['IDParametro'],
                'Resultado': f"Resultado {random.randint(1,100)}",
                'FechaResultado': random_date(),
                'NombreParametro': param['NombreParametro']
            })
            id_res += 1
    return resultados