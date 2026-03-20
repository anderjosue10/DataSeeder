import pandas as pd
import json
import io

def generate_sql(*dfs):
    sql = ""
    tables = ['Cliente', 'Medico', 'Orden', 'DetalleOrden', 'Factura', 'DetalleFactura', 'ResultadoExamen']
    for df, table in zip(dfs, tables):
        sql += f"INSERT INTO {table} ({', '.join(df.columns)}) VALUES\n"
        values = []
        for _, row in df.iterrows():
            vals = []
            for val in row:
                if isinstance(val, str):
                    vals.append(f"'{val}'")
                elif pd.isna(val):
                    vals.append('NULL')
                else:
                    vals.append(str(val))
            values.append(f"({', '.join(vals)})")
        sql += ',\n'.join(values) + ';\n\n'
    return sql

def export_json(data):
    return json.dumps(data, indent=4, default=str)

def export_csv(data):
    all_data = []
    for table, records in data.items():
        for record in records:
            all_data.append({'Tabla': table, **record})
    df_all = pd.DataFrame(all_data)
    csv_buffer = io.StringIO()
    df_all.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)
    return csv_buffer.getvalue()