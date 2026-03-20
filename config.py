# Configuration file
import os

# Database settings (if needed)
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'LaboratorioClinico')

# Generation parameters
DEFAULT_NUM_CLIENTES = 10
DEFAULT_NUM_MEDICOS = 5
DEFAULT_NUM_ORDENES = 20
DEFAULT_NUM_FACTURAS = 15

# Faker settings
LOCALE = 'es_ES'