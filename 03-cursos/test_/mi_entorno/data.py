import pandas as pd
import os

# Leer el archivo Excel
archivo_entrada = 'data_q.xlsx'
df = pd.read_excel(archivo_entrada)

# Convertir la columna de fecha a datetime
df['Data'] = pd.to_datetime(df['Data'])

# Agregar columnas de año y mes
df['Año'] = df['Data'].dt.year
df['Mes'] = df['Data'].dt.month

# Calcular promedios anuales por estación
promedio_anual = df.groupby(['EstacaoCodigo', 'Año']).agg({
    'Maxima': 'mean',
    'Minima': 'mean',
    'Media': 'mean'
}).reset_index()

# Calcular promedios mensuales por estación y año
promedio_mensual = df.groupby(['EstacaoCodigo', 'Año', 'Mes']).agg({
    'Maxima': 'mean',
    'Minima': 'mean',
    'Media': 'mean'
}).reset_index()

# Guardar resultados en un nuevo archivo Excel
with pd.ExcelWriter(archivo_entrada, mode='a') as writer:
    promedio_anual.to_excel(writer, sheet_name='pa', index=False)
    promedio_mensual.to_excel(writer, sheet_name='pma', index=False)

print("Proceso completado. Resultados guardados en hojas 'pa' y 'pma' de data_q.xlsx")