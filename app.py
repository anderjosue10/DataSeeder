from flask import Flask, render_template, request, send_file
import io
import pandas as pd
from generators.employees import generate_clientes
from generators.salaries import generate_medicos
from generators.departments import generate_ordenes
from generators.titles import generate_detalle_ordenes
from generators.dept_emp import generate_facturas, generate_detalle_facturas, generate_resultados
from generators.dirty_generators import (
    generate_clientes_dirty, generate_medicos_dirty, generate_ordenes_dirty,
    generate_detalle_ordenes_dirty, generate_facturas_dirty,
    generate_detalle_facturas_dirty, generate_resultados_dirty
)
from services.db_writer import generate_sql, export_json, export_csv
from services.validator import validate_data
from services.progress import ProgressMonitor
from config import DEFAULT_NUM_CLIENTES, DEFAULT_NUM_MEDICOS, DEFAULT_NUM_ORDENES, DEFAULT_NUM_FACTURAS

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    progress = ProgressMonitor()
    progress.update("Iniciando generación de datos")

    num_clientes = int(request.form.get('num_clientes', DEFAULT_NUM_CLIENTES))
    num_medicos = int(request.form.get('num_medicos', DEFAULT_NUM_MEDICOS))
    num_ordenes = int(request.form.get('num_ordenes', DEFAULT_NUM_ORDENES))
    num_facturas = int(request.form.get('num_facturas', DEFAULT_NUM_FACTURAS))
    format_type = request.form.get('format', 'json')
    data_type = request.form.get('data_type', 'clean')

    if data_type == 'dirty':
        progress.update("Generando clientes con datos sucios")
        clientes = generate_clientes_dirty(num_clientes)

        progress.update("Generando médicos con datos sucios")
        medicos = generate_medicos_dirty(num_medicos)

        progress.update("Generando órdenes con datos sucios")
        ordenes = generate_ordenes_dirty(num_ordenes, clientes, medicos)

        progress.update("Generando detalles de orden con datos sucios")
        detalles_orden = generate_detalle_ordenes_dirty(num_ordenes, ordenes)

        progress.update("Generando facturas con datos sucios")
        facturas = generate_facturas_dirty(num_facturas, clientes, medicos, ordenes)

        progress.update("Generando detalles de factura con datos sucios")
        detalles_fact = generate_detalle_facturas_dirty(facturas, detalles_orden)

        progress.update("Generando resultados con datos sucios")
        resultados = generate_resultados_dirty(detalles_orden, [{'IDParametro': 1, 'IDTipoExamen': 1, 'NombreParametro': 'Proteína C Reactiva (PCR)', 'Precio': 100.00}, {'IDParametro': 4, 'IDTipoExamen': 2, 'NombreParametro': 'Eritrocitos', 'Precio': 15.00}, {'IDParametro': 18, 'IDTipoExamen': 3, 'NombreParametro': 'Color', 'Precio': 25.00}])

        progress.update("Omitiendo validación para datos sucios")
    else:
        progress.update("Generando clientes")
        clientes = generate_clientes(num_clientes)

        progress.update("Generando médicos")
        medicos = generate_medicos(num_medicos)

        progress.update("Generando órdenes")
        ordenes = generate_ordenes(num_ordenes, clientes, medicos)

        progress.update("Generando detalles de orden")
        detalles_orden = generate_detalle_ordenes(num_ordenes, ordenes)

        progress.update("Generando facturas")
        facturas = generate_facturas(num_facturas, clientes, medicos, ordenes)

        progress.update("Generando detalles de factura")
        detalles_fact = generate_detalle_facturas(facturas, detalles_orden)

        progress.update("Generando resultados")
        resultados = generate_resultados(detalles_orden, [{'IDParametro': 1, 'IDTipoExamen': 1, 'NombreParametro': 'Proteína C Reactiva (PCR)', 'Precio': 100.00}, {'IDParametro': 4, 'IDTipoExamen': 2, 'NombreParametro': 'Eritrocitos', 'Precio': 15.00}, {'IDParametro': 18, 'IDTipoExamen': 3, 'NombreParametro': 'Color', 'Precio': 25.00}])

        progress.update("Validando datos")
        errors = validate_data(clientes, medicos, ordenes, detalles_orden, facturas, detalles_fact, resultados)
        if errors:
            progress.update(f"Errores encontrados: {len(errors)}")
            for error in errors[:5]:  # Mostrar primeros 5
                progress.update(error)
            return "Errores en validación", 400

    data = {
        'clientes': clientes,
        'medicos': medicos,
        'ordenes': ordenes,
        'detalles_orden': detalles_orden,
        'facturas': facturas,
        'detalles_factura': detalles_fact,
        'resultados': resultados
    }

    if format_type == 'json':
        json_str = export_json(data)
        progress.finish()
        return send_file(io.BytesIO(json_str.encode()), as_attachment=True, download_name='datos.json', mimetype='application/json')
    
    elif format_type == 'csv':
        csv_str = export_csv(data)
        progress.finish()
        return send_file(io.BytesIO(csv_str.encode()), as_attachment=True, download_name='datos.csv', mimetype='text/csv')
    
    elif format_type == 'sql':
        df_clientes = pd.DataFrame(clientes)
        df_medicos = pd.DataFrame(medicos)
        df_ordenes = pd.DataFrame(ordenes)
        df_detalles_orden = pd.DataFrame(detalles_orden)
        df_facturas = pd.DataFrame(facturas)
        df_detalles_fact = pd.DataFrame(detalles_fact)
        df_resultados = pd.DataFrame(resultados)
        
        sql = generate_sql(df_clientes, df_medicos, df_ordenes, df_detalles_orden, df_facturas, df_detalles_fact, df_resultados)
        progress.finish()
        return send_file(io.BytesIO(sql.encode()), as_attachment=True, download_name='datos.sql', mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)