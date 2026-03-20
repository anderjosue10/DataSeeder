def validate_data(clientes, medicos, ordenes, detalles_orden, facturas, detalles_fact, resultados):
    # Validar que IDs existen
    cliente_ids = {c['IDCliente'] for c in clientes}
    medico_ids = {m['IDMedico'] for m in medicos}
    orden_ids = {o['IDOrden'] for o in ordenes}
    detalle_orden_ids = {do['IDDetalleOrden'] for do in detalles_orden}
    factura_ids = {f['IDFactura'] for f in facturas}

    errors = []

    for o in ordenes:
        if o['IDCliente'] not in cliente_ids:
            errors.append(f"Orden {o['IDOrden']} referencia cliente inexistente {o['IDCliente']}")
        if o['IDMedico'] not in medico_ids:
            errors.append(f"Orden {o['IDOrden']} referencia medico inexistente {o['IDMedico']}")

    for do in detalles_orden:
        if do['IDOrden'] not in orden_ids:
            errors.append(f"DetalleOrden {do['IDDetalleOrden']} referencia orden inexistente {do['IDOrden']}")

    for f in facturas:
        if f['IDCliente'] not in cliente_ids:
            errors.append(f"Factura {f['IDFactura']} referencia cliente inexistente {f['IDCliente']}")
        if f['IDMedico'] not in medico_ids:
            errors.append(f"Factura {f['IDFactura']} referencia medico inexistente {f['IDMedico']}")

    for df in detalles_fact:
        if df['IDFactura'] not in factura_ids:
            errors.append(f"DetalleFactura {df['IDDetalleFactura']} referencia factura inexistente {df['IDFactura']}")
        if df['IDDetalleOrden'] not in detalle_orden_ids:
            errors.append(f"DetalleFactura {df['IDDetalleFactura']} referencia detalle orden inexistente {df['IDDetalleOrden']}")

    for r in resultados:
        if r['IDDetalleOrden'] not in detalle_orden_ids:
            errors.append(f"Resultado {r['IDResultado']} referencia detalle orden inexistente {r['IDDetalleOrden']}")

    return errors