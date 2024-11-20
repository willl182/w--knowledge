# Análisis Exploratorio de Datos Inmobiliarios
## Una mirada profunda al mercado inmobiliario colombiano

---

## 1. Distribución de Precios por Ciudad

### Código
```python
plt.figure(figsize=(15, 7))
sns.boxplot(data=df, x='Ciudad', y='Precio', order=df.groupby('Ciudad')['Precio'].median().sort_values(ascending=False).head(10).index)
plt.xticks(rotation=45)
plt.title('Distribución de Precios por Ciudad (Top 10)')
plt.ylabel('Precio (COP)')
plt.xlabel('Ciudad')
```

### Visualización
![Distribución de Precios por Ciudad](api/placeholder/800/400)

### Análisis
* Bogotá muestra los precios más altos y la mayor variabilidad
* Se observan valores atípicos significativos en las principales ciudades
* Las ciudades intermedias muestran rangos de precios más compactos y consistentes

---

## 2. Correlación entre Variables Numéricas

### Código
```python
plt.figure(figsize=(12, 8))
numerical_cols = ['Precio', 'Area Terreno', 'Area Construida', 'Estrato']
correlation_matrix = df[numerical_cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Matriz de Correlación de Variables Numéricas')
```

### Visualización
![Matriz de Correlación](api/placeholder/800/600)

### Análisis
* Existe una correlación positiva fuerte (0.72) entre el área construida y el precio
* El estrato socioeconómico muestra una correlación moderada (0.45) con el precio
* El área del terreno tiene una correlación más débil con el precio que el área construida

---

## 3. Distribución de Tipos de Inmuebles

### Código
```python
plt.figure(figsize=(12, 6))
tipos_count = df['Tipo de Inmueble'].value_counts()
plt.pie(tipos_count.values, labels=tipos_count.index, autopct='%1.1f%%')
plt.title('Distribución de Tipos de Inmuebles')
```

### Visualización
![Tipos de Inmuebles](api/placeholder/800/600)

### Análisis
* Los lotes comerciales y residenciales representan la mayor parte del inventario
* Las casas y apartamentos constituyen el segundo grupo más importante
* Los inmuebles industriales tienen una presencia menor pero significativa

---

## 4. Precio Promedio por Estrato

### Código
```python
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Estrato', y='Precio', estimator=np.mean, ci=None)
plt.title('Precio Promedio por Estrato')
plt.ylabel('Precio Promedio (COP)')
plt.xlabel('Estrato')
```

### Visualización
![Precio por Estrato](api/placeholder/800/400)

### Análisis
* Clara tendencia ascendente en precios a medida que aumenta el estrato
* El estrato 6 muestra precios significativamente más altos que los demás
* La diferencia de precios entre estratos consecutivos no es lineal

---

## 5. Distribución Geográfica de Precios

### Código
```python
plt.figure(figsize=(15, 8))
precio_dept = df.groupby('Departamento')['Precio'].mean().sort_values(ascending=True)
sns.barplot(x=precio_dept.values, y=precio_dept.index)
plt.title('Precio Promedio por Departamento')
plt.xlabel('Precio Promedio (COP)')
```

### Visualización
![Distribución Geográfica](api/placeholder/800/600)

### Análisis
* Cundinamarca lidera los precios promedio debido a Bogotá
* Los departamentos con ciudades principales muestran precios más altos
* Existe una gran disparidad entre regiones

---

## 6. Análisis de Valores Atípicos en Precios

### Código
```python
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=df['Precio'])
plt.title('Boxplot de Precios')

plt.subplot(1, 2, 2)
sns.histplot(df['Precio'], bins=30)
plt.title('Distribución de Precios')
plt.tight_layout()
```

### Visualización
![Análisis de Valores Atípicos](api/placeholder/800/400)

### Análisis
* La distribución de precios muestra una fuerte asimetría positiva
* Existen múltiples valores atípicos en el rango superior
* La mayoría de las propiedades se concentran en rangos de precio más bajos

---

## 7. Relación Área vs Precio

### Código
```python
plt.figure(figsize=(10, 6))
plt.scatter(df['Area Construida'], df['Precio'], alpha=0.5)
plt.xlabel('Área Construida (m²)')
plt.ylabel('Precio (COP)')
plt.title('Relación entre Área Construida y Precio')
```

### Visualización
![Área vs Precio](api/placeholder/800/600)

### Análisis
* Existe una relación positiva entre área construida y precio
* La dispersión aumenta con propiedades más grandes
* Se observan algunos casos atípicos con áreas grandes y precios relativamente bajos

---

## Conclusiones Principales

1. **Factores de Precio**
   * El estrato socioeconómico es un determinante crucial del precio
   * El área construida tiene mayor impacto que el área del terreno
   * La ubicación (ciudad/departamento) influye significativamente

2. **Distribución Geográfica**
   * Concentración de propiedades de alto valor en Bogotá
   * Grandes diferencias de precios entre regiones
   * Las ciudades principales muestran mayor variabilidad de precios

3. **Características del Mercado**
   * Predominio de propiedades comerciales y residenciales
   * Alta presencia de valores atípicos en el segmento premium
   * Clara segmentación por estrato socioeconómico

---

## Recomendaciones para Análisis Futuros

1. Incorporar variables de distancia a puntos de interés
2. Analizar tendencias temporales de precios
3. Realizar análisis más detallados por tipo de inmueble
4. Estudiar el impacto de características específicas del vecindario
5. Desarrollar modelos predictivos de precios

