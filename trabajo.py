import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Leer el archivo Excel
archivo_excel = r'C:\Users\Sergi\OneDrive\Documentos\Consumo.xlsx'
datos_excel = pd.read_excel(archivo_excel)

# Gráfico de barras utilizando Seaborn para mostrar la distribución de estratos
plt.figure(figsize=(10, 6))
sns.countplot(x='ESTRATO', data=datos_excel, palette='coolwarm')
plt.title('Distribución de Estratos')
plt.xlabel('Estrato')
plt.ylabel('Cantidad')
plt.grid(True)
plt.show()

# Gráfico de barras utilizando Plotly para mostrar la distribución de consumo de agua por municipio
fig = px.bar(datos_excel, x='MUNICIPIO', y='CONSUMO M3 ACUEDUCTO', title='Consumo de Agua por Municipio',
             labels={'CONSUMO M3 ACUEDUCTO': 'Consumo de agua (m3)'}, color='MUNICIPIO')
fig.update_xaxes(tickangle=45)
fig.show()

# Gráfico de dispersión utilizando Plotly para mostrar la relación entre consumo de agua y consumo de alcantarillado
fig = px.scatter(datos_excel, x='CONSUMO M3 ACUEDUCTO', y='PROMEDIO CONSUMO ALCANTARILLADO',
                 title='Consumo de Agua vs Consumo de Alcantarillado', labels={'CONSUMO M3 ACUEDUCTO': 'Consumo de agua (m3)',
                                                                                'PROMEDIO CONSUMO ALCANTARILLADO': 'Promedio consumo alcantarillado'})
fig.show()

# Gráfico de distribución del consumo de agua por año
plt.figure(figsize=(10, 6))
sns.histplot(data=datos_excel, x='AÃ‘O', y='CONSUMO M3 ACUEDUCTO', bins=20, kde=True)
plt.title('Distribución del Consumo de Agua por Año')
plt.xlabel('Año')
plt.ylabel('Consumo de agua (m3)')
plt.grid(True)
plt.show()

# Gráfico de boxplot para comparar el consumo de agua por estrato
plt.figure(figsize=(10, 6))
sns.boxplot(data=datos_excel, x='ESTRATO', y='CONSUMO M3 ACUEDUCTO', palette='viridis')
plt.title('Comparación del Consumo de Agua por Estrato')
plt.xlabel('Estrato')
plt.ylabel('Consumo de agua (m3)')
plt.grid(True)
plt.show()

# Gráfico de dispersión 3D para explorar la relación entre consumo de agua, estrato y municipio
fig = px.scatter_3d(datos_excel, x='CONSUMO M3 ACUEDUCTO', y='ESTRATO', z='MUNICIPIO',
                    title='Relación entre Consumo de Agua, Estrato y Municipio')
fig.update_traces(marker=dict(size=5))
fig.show()