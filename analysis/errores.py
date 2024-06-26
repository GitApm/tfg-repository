import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Cargar el archivo CSV
df = pd.read_csv('Analisis.csv')

# Calcular la línea de tendencia
slope, intercept, _, _, _ = linregress(df['Numero_Observaciones'], df['errores'])
tendencia = slope * df['Numero_Observaciones'] + intercept

# Crear la cadena que representa la pendiente
pendiente_str = 'Pendiente: {:.2f}'.format(slope)

# Graficar los datos y la línea de tendencia
plt.scatter(df['Numero_Observaciones'], df['errores'], label='Datos')
plt.plot(df['Numero_Observaciones'], tendencia, color='red', label='Línea de tendencia')
plt.xlim(0, df['Numero_Observaciones'].max()+50)
plt.ylim(0, df['errores'].max()+5)
plt.text(10, df['errores'].max()+2, pendiente_str, color='red', fontsize=10)
plt.xlabel('Número de Acciones')
plt.ylabel('Número de errores')
plt.title('Acciones vs errores')
plt.grid(True)
plt.show()
