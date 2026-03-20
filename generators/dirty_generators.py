import random
from datetime import datetime, timedelta
from utils.faker_helpers import random_name, random_date, random_phone

# Datos sucios - con campos null, datos inválidos, etc.

def generate_clientes_dirty(num):
    """Genera clientes con datos sucios: campos null, nombres inválidos, etc."""
    clientes = []
    for i in range(1, num + 1):
        # 20% de probabilidad de campos null o inválidos
        if random.random() < 0.2:
            nombre = None
        elif random.random() < 0.1:
            nombre = "INVALID_NAME_123!@#"
        else:
            nombre = random_name()

        if random.random() < 0.15:
            fecha_nac = None
        elif random.random() < 0.1:
            fecha_nac = datetime(1900, 1, 1)  # Fecha muy antigua
        else:
            fecha_nac = random_date()

        if random.random() < 0.1:
            genero = None
        elif random.random() < 0.05:
            genero = "X"  # Género inválido
        else:
            genero = random.choice(['M', 'F'])

        if random.random() < 0.2:
            telefono = None
        elif random.random() < 0.1:
            telefono = "INVALID_PHONE"
        else:
            telefono = random_phone()

        clientes.append({
            'IDCliente': i,
            'Nombre': nombre,
            'FechaNacimiento': fecha_nac,
            'Genero': genero,
            'Telefono': telefono
        })
    return clientes

def generate_medicos_dirty(num):
    """Genera médicos con datos sucios"""
    medicos = []
    for i in range(1, num + 1):
        if random.random() < 0.2:
            nombre = None
        else:
            nombre = random_name()

        if random.random() < 0.15:
            especialidad = None
        elif random.random() < 0.1:
            especialidad = "INVALID_SPECIALTY"
        else:
            especialidad = random.choice(['MEDICO', 'BIOANALISTA'])

        if random.random() < 0.1:
            password = None
        else:
            password = 'hashed_password'

        if random.random() < 0.2:
            telefono = None
        else:
            telefono = random_phone()

        if random.random() < 0.1:
            rol = None
        else:
            rol = random.choice(['EMPLEADO', 'ADMIN'])

        if random.random() < 0.15:
            correo = None
        elif random.random() < 0.1:
            correo = "invalid-email"
        else:
            correo = f"{random_name().replace(' ', '').lower()}@gmail.com"

        medicos.append({
            'IDMedico': i,
            'Nombre': nombre,
            'Especialidad': especialidad,
            'Password': password,
            'Telefono': telefono,
            'Rol': rol,
            'Correo': correo,
            'ContrasenaTemporal': random.choice([True, False])
        })
    return medicos

def generate_ordenes_dirty(num, clientes, medicos):
    """Genera órdenes con datos sucios - posibles referencias inválidas"""
    ordenes = []
    for i in range(1, num + 1):
        # 10% de probabilidad de ID cliente inválido
        if random.random() < 0.1:
            id_cliente = random.randint(9999, 99999)  # ID que no existe
        else:
            id_cliente = random.choice(clientes)['IDCliente']

        # 10% de probabilidad de ID médico inválido
        if random.random() < 0.1:
            id_medico = random.randint(9999, 99999)  # ID que no existe
        else:
            id_medico = random.choice(medicos)['IDMedico']

        fecha_orden = random_date()

        if random.random() < 0.1:
            estado = None
        elif random.random() < 0.05:
            estado = "INVALID_STATUS"
        else:
            estado = 'COMPLETADO'

        if random.random() < 0.15:
            fecha_entrega = None
        else:
            fecha_entrega = fecha_orden + timedelta(days=random.randint(1,7))

        if random.random() < 0.1:
            numero_muestra = None
        else:
            numero_muestra = random.randint(1,4)

        ordenes.append({
            'IDOrden': i,
            'IDCliente': id_cliente,
            'IDMedico': id_medico,
            'FechaOrden': fecha_orden,
            'Estado': estado,
            'fechaEntrega': fecha_entrega,
            'NumeroMuestra': numero_muestra
        })
    return ordenes

def generate_detalle_ordenes_dirty(num, ordenes):
    """Genera detalles de orden con datos sucios"""
    detalles = []
    id_det = 1
    for orden in ordenes:
        num_det = random.randint(1,3)
        for _ in range(num_det):
            if random.random() < 0.1:
                id_orden = random.randint(9999, 99999)  # Orden que no existe
            else:
                id_orden = orden['IDOrden']

            if random.random() < 0.15:
                id_tipo_examen = None
            else:
                id_tipo_examen = random.randint(1, 13)

            if random.random() < 0.1:
                id_muestra = None
            else:
                id_muestra = random.randint(1, 4)

            detalles.append({
                'IDDetalleOrden': id_det,
                'IDOrden': id_orden,
                'IDTipoExamen': id_tipo_examen,
                'IDMuestra': id_muestra
            })
            id_det += 1
    return detalles

def generate_facturas_dirty(num, clientes, medicos, ordenes):
    """Genera facturas con datos sucios"""
    facturas = []
    for i in range(1, num + 1):
        if random.random() < 0.1:
            orden = {'FechaOrden': random_date(), 'IDCliente': random.choice(clientes)['IDCliente'], 'IDMedico': random.choice(medicos)['IDMedico']}
        else:
            orden = random.choice(ordenes)

        if random.random() < 0.15:
            fecha_fact = None
        else:
            fecha_fact = orden['FechaOrden'] + timedelta(days=random.randint(1,10))

        if random.random() < 0.1:
            total = None
        elif random.random() < 0.05:
            total = -100.00  # Total negativo
        else:
            total = round(random.uniform(100, 1000), 2)

        if random.random() < 0.1:
            tipo_facturacion = None
        elif random.random() < 0.05:
            tipo_facturacion = "INVALID_TYPE"
        else:
            tipo_facturacion = random.choice(['EXAMEN', 'PARAMETRO'])

        facturas.append({
            'IDFactura': i,
            'IDCliente': orden['IDCliente'],
            'FechaFactura': fecha_fact,
            'Total': total,
            'IDMedico': orden['IDMedico'],
            'TipoFacturacion': tipo_facturacion
        })
    return facturas

def generate_detalle_facturas_dirty(facturas, detalles_orden):
    """Genera detalles de factura con datos sucios"""
    detalles_fact = []
    id_det_fact = 1
    for factura in facturas:
        num_det = random.randint(1,3)
        for _ in range(num_det):
            if random.random() < 0.1:
                id_detalle_orden = random.randint(9999, 99999)  # ID que no existe
            else:
                id_detalle_orden = random.choice(detalles_orden)['IDDetalleOrden']

            if random.random() < 0.15:
                subtotal = None
            else:
                subtotal = round(random.uniform(50, 500), 2)

            if random.random() < 0.1:
                precio = None
            else:
                precio = round(random.uniform(50, 500), 2)

            if random.random() < 0.2:
                nombre_parametro = None
            elif random.random() < 0.1:
                nombre_parametro = "INVALID_PARAM"
            else:
                nombre_parametro = random.choice(['UROANALISIS', 'HEMATOLOGÍA', 'SEROLOGÍA'])

            detalles_fact.append({
                'IDDetalleFactura': id_det_fact,
                'IDFactura': factura['IDFactura'],
                'IDDetalleOrden': id_detalle_orden,
                'Subtotal': subtotal,
                'Precio': precio,
                'NombreParametro': nombre_parametro,
                'Idparametro': random.randint(1, 20),
                'IdtipoExamen': random.randint(1, 13)
            })
            id_det_fact += 1
    return detalles_fact

def generate_resultados_dirty(detalles_orden, parametros):
    """Genera resultados con datos sucios"""
    resultados = []
    id_res = 1
    for det in detalles_orden:
        num_res = random.randint(1,5)
        for _ in range(num_res):
            if random.random() < 0.1:
                id_detalle_orden = random.randint(9999, 99999)  # ID que no existe
            else:
                id_detalle_orden = det['IDDetalleOrden']

            param = random.choice(parametros)

            if random.random() < 0.2:
                resultado = None
            elif random.random() < 0.1:
                resultado = "INVALID_RESULT_!@#"
            else:
                resultado = f"Resultado {random.randint(1,100)}"

            if random.random() < 0.15:
                fecha_resultado = None
            else:
                fecha_resultado = random_date()

            resultados.append({
                'IDResultado': id_res,
                'IDDetalleOrden': id_detalle_orden,
                'IDParametro': param['IDParametro'],
                'Resultado': resultado,
                'FechaResultado': fecha_resultado,
                'NombreParametro': param['NombreParametro']
            })
            id_res += 1
    return resultados