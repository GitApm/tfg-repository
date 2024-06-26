import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Cargar el archivo CSV
df = pd.read_csv('Time_Acciones.csv')

# Calcular la línea de tendencia
slope, intercept, _, _, _ = linregress(df['Tiempo'], df['Numero_Observaciones'])
tendencia = slope * df['Tiempo'] + intercept

# Crear la cadena que representa la pendiente
pendiente_str = 'Pendiente: {:.2f}'.format(slope)

# Graficar los datos y la línea de tendencia
plt.scatter(df['Tiempo'], df['Numero_Observaciones'], label='Datos')
plt.plot(df['Tiempo'], tendencia, color='red', label='Línea de tendencia')
plt.text(50, df['Numero_Observaciones'].max()+30, pendiente_str, color='red', fontsize=10)
plt.xlim(0, df['Tiempo'].max()+50)
plt.ylim(0, df['Numero_Observaciones'].max()+50)
plt.xlabel('Duración de la partida')
plt.ylabel('Número de Acciones')
plt.title('Duración vs Número de Acciones')
plt.grid(True)
plt.show()
