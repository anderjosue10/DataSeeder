# Generador de Datos Sintéticos para Laboratorio Clínico

Aplicación web en Flask que genera datos sintéticos masivos para una base de datos de laboratorio clínico, manteniendo integridad referencial y coherencia temporal.

## Instalación

1. Instalar dependencias:
   pip install -r requirements.txt

2. Ejecutar la aplicación:
   python app.py

3. Abrir en navegador: http://127.0.0.1:5000/

## Uso

- Ingresar números de registros para cada entidad.
- Hacer clic en "Generar y Descargar Datos (JSON)" para obtener un archivo JSON con los datos generados.

## Características

- Genera datos para tablas: Cliente, Medico, Orden, DetalleOrden, Factura, DetalleFactura, ResultadoExamen.
- Mantiene claves foráneas.
- Coherencia temporal: fechas de órdenes antes de facturas, etc.
- Exportación a JSON (puede extenderse a CSV y SQL).

## Notas

- Datos simplificados para rapidez.
- Usar Faker para datos realistas.