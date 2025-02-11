import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo Excel, específicamente la hoja 'pa'
df = pd.read_excel('data_q.xlsx', sheet_name='pa')

# Configurar el estilo y tamaño de la figura
plt.figure(figsize=(15, 10))

# Crear subplots para cada variable
variables = ['Maxima', 'Minima', 'Media']
for i, variable in enumerate(variables, 1):
    plt.subplot(1, 3, i)
    
    # Crear diagrama de caja usando seaborn
    sns.boxplot(x='Año', y=variable, data=df)
    
    # Personalizar el subplot
    plt.title(f'Diagrama de Caja - {variable}')
    plt.xticks(rotation=45)
    plt.xlabel('Año')
    plt.ylabel(variable)

# Ajustar el espacio entre subplots
plt.tight_layout()

# Guardar la figura
plt.savefig('diagramas_caja_por_año.png')

# Mostrar la figura (opcional, útil si estás corriendo el script en un entorno interactivo)
plt.show()

print("Diagramas de caja generados y guardados como 'diagramas_caja_por_año.png'")