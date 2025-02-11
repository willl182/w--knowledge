import pandas as pd
import os

# Obtener el directorio actual
directorio_actual = os.getcwd()

# Nombre del archivo de entrada
archivo_entrada = 'data.xlsx'

# Lista para almacenar todos los DataFrames
dataframes = []

# Leer todas las hojas del archivo Excel
excel = pd.ExcelFile(os.path.join(directorio_actual, archivo_entrada))

# Iterar sobre todas las hojas del archivo
for nombre_hoja in excel.sheet_names:
    df = pd.read_excel(excel, sheet_name=nombre_hoja)
    dataframes.append(df)

# Concatenar todos los DataFrames
datos_consolidados = pd.concat(dataframes, ignore_index=True)

# Guardar los datos consolidados en una nueva hoja del mismo archivo Excel
with pd.ExcelWriter(os.path.join(directorio_actual, archivo_entrada), mode='a') as writer:
    datos_consolidados.to_excel(writer, sheet_name='Datos_Consolidados', index=False)

print("Proceso completado. Datos consolidados guardados en una nueva hoja de data.xlsx")