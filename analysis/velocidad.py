import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Cargar el archivo CSV
df = pd.read_csv('Analisis.csv')

# Calcular la línea de tendencia
slope, intercept, _, _, _ = linregress(df['Tiempo'], df['procesado'])
tendencia = slope * df['Tiempo'] + intercept

# Crear la cadena que representa la pendiente
pendiente_str = 'Pendiente: {:.2f}'.format(slope)

# Graficar los datos y la línea de tendencia
plt.scatter(df['Tiempo'], df['procesado'], label='Datos')
plt.plot(df['Tiempo'], tendencia, color='red', label='Línea de tendencia')
plt.xlim(0, df['Tiempo'].max()+50)
plt.ylim(0, df['procesado'].max()+205)
plt.text(10, df['procesado'].max(), pendiente_str, color='red', fontsize=10)
plt.xlabel('Duración de la partida')
plt.ylabel('Tiempo de procesado')
plt.title('Duración partida vs procesado')
plt.grid(True)
plt.show()