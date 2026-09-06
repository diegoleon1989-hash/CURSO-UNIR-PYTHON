import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. Configuración y Carga de Datos
# ==========================================
# Cargar el dataset asumiendo que está en el mismo directorio
df = pd.read_csv('superstore_dataset2012.csv')

# ==========================================
# 2. Exploración y Preparación de los Datos
# ==========================================
print("--- Información General del Dataset ---")
print(df.info())
print("\n--- Conteo de Valores Nulos ---")
print(df.isnull().sum())

# Tratamiento de datos: 'Postal Code' tiene una gran cantidad de nulos, por lo que la omitiremos
df = df.drop(columns=['Postal Code'])

# Convertir la columna de fecha 'Order Date' al formato adecuado (datetime)
# Usamos dayfirst=True debido al formato original de los datos
df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed', dayfirst=True)

# ==========================================
# 3. Creación de Visualizaciones en Subplots
# ==========================================
# Configurar el estilo de Seaborn para gráficos más limpios
sns.set_theme(style="whitegrid")

# Crear una figura con 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Análisis de Rendimiento - Superstore 2012', fontsize=20, fontweight='bold')

# --- Gráfico 1: Univariante con Matplotlib (Histograma) ---
# Mostramos la distribución de las Ventas. Filtramos ventas menores a 1500 para evitar que los outliers extremos aplasten el gráfico.
axes[0, 0].hist(df[df['Sales'] < 1500]['Sales'], bins=30, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Distribución de Ventas (Matplotlib)')
axes[0, 0].set_xlabel('Ventas ($)')
axes[0, 0].set_ylabel('Frecuencia')
# Conclusión: La distribución está fuertemente sesgada a la derecha. La inmensa mayoría de las transacciones son por montos pequeños (menos de $200).

# --- Gráfico 2: Univariante con Seaborn (Boxplot) ---
# Visualizamos la distribución de Beneficios por Categoría de producto
sns.boxplot(data=df, x='Category', y='Profit', ax=axes[0, 1], palette='Set2')
axes[0, 1].set_title('Beneficios por Categoría (Seaborn)')
axes[0, 1].set_ylim(-500, 500) # Limitamos el eje Y para poder ver bien las cajas
axes[0, 1].set_xlabel('Categoría')
axes[0, 1].set_ylabel('Beneficio ($)')
# Conclusión: La categoría "Technology" tiene una mediana de beneficios más alta, pero también una dispersión considerable. "Furniture" tiene muchos valores atípicos negativos (pérdidas).

# --- Gráfico 3: Bivariante con Matplotlib (Gráfico de Dispersión) ---
# Relación entre Ventas y Beneficios
axes[1, 0].scatter(df['Sales'], df['Profit'], alpha=0.5, color='coral', edgecolor='white')
axes[1, 0].set_title('Relación: Ventas vs Beneficios (Matplotlib)')
axes[1, 0].set_xlabel('Ventas ($)')
axes[1, 0].set_ylabel('Beneficio ($)')
# Conclusión: A medida que aumentan las ventas, los beneficios tienden a aumentar, pero también el riesgo; se observan casos de grandes pérdidas en ventas de alto volumen.

# --- Gráfico 4: Bivariante con Seaborn (Barplot Agrupado) ---
# Ventas promedio por Segmento y Categoría
sns.barplot(data=df, x='Segment', y='Sales', hue='Category', ax=axes[1, 1], palette='viridis', errorbar=None)
axes[1, 1].set_title('Ventas Promedio por Segmento y Categoría (Seaborn)')
axes[1, 1].set_xlabel('Segmento')
axes[1, 1].set_ylabel('Ventas Promedio ($)')
# Conclusión: El segmento "Home Office" y "Corporate" en la categoría de Tecnología son los que presentan el mayor promedio de ventas por transacción.

# Ajustar el espacio entre los gráficos para que no se superpongan los textos
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Guardar y documentar la figura principal
plt.savefig('analisis_rendimiento_superstore.png', dpi=300)
print("\n✅ Imagen guardada: 'analisis_rendimiento_superstore.png'")

# ==========================================
# 4. Visualización Multivariante (Heatmap)
# ==========================================
# Crear una figura separada para el Heatmap de correlaciones
plt.figure(figsize=(8, 6))

# Seleccionar solo las columnas numéricas para calcular la correlación
columnas_numericas = ['Sales', 'Quantity', 'Discount', 'Profit', 'Shipping Cost']
matriz_correlacion = df[columnas_numericas].corr()

# Crear el heatmap usando Seaborn
sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0, fmt='.2f')
plt.title('Mapa de Calor de Correlaciones Numéricas (Seaborn)', fontsize=14, fontweight='bold')
plt.tight_layout()

# Guardar y documentar el heatmap
plt.savefig('mapa_calor_superstore.png', dpi=300)
print("✅ Imagen guardada: 'mapa_calor_superstore.png'")

# Conclusión Multivariante: Existe una fuerte correlación positiva (0.76) entre las Ventas y el Costo de Envío, lo que indica que envíos más costosos se asocian a pedidos de mayor volumen. También hay una correlación negativa entre el Descuento y el Beneficio, indicando que mayores descuentos erosionan el margen.