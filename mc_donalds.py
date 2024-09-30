import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

uploaded = files.upload()

for filename in uploaded.keys():
    #Path de donde esta el archivo excel
    filename = "mcdonalds.xlsx"

    df['Hour'] = pd.to_timedelta(df['Hora de Arribo']).dt.components['hours']

    plt.figure(figsize=(14, 6))

    #FDP para Hora de Arribo de los Clientes Total

    plt.subplot(1, 2, 1)
    sns.histplot(df['Hour'], bins=range(0, 25, 2), stat='count', kde=True)
    plt.title('Frecuencia de clientes por Hora de Arribo')
    plt.xlabel('Hora de Arribo')
    plt.ylabel('Frecuencia')

    plt.xticks(range(0, 25, 2))
    plt.grid(axis='y')

    #FDP para Tiempo de Atencion de los Clientes Total

    plt.subplot(1, 2, 2)
    sns.histplot(df['Tiempo de Atención'], bins=range(0, int(df['Tiempo de Atención'].max()) + 30, 30), stat='count', kde=True)
    plt.title('Frecuencia de Tiempo de Atención en Segundos')
    plt.xlabel('Tiempo de Atención')
    plt.ylabel('Frecuencia')

    plt.tight_layout()
    plt.show()

    #FDP para Hora de Arribo de los Clientes atendidos por cajeros

    df_h = df[df['Tipo de Atención'] == 'h']

    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    sns.histplot(df_h['Hour'], bins=range(0, 25, 2), stat='count', kde=True)
    plt.title('Frecuencia de clientes por Hora de Arribo de Puesto de Atención')
    plt.xlabel('Hora de Arribo')
    plt.ylabel('Frecuencia')
    plt.xticks(range(0, 25, 2))
    plt.grid(axis='y')

    #FDP para Tiempo de Atencion de los Clientes atendidos por cajeros

    plt.subplot(1, 2, 2)
    sns.histplot(df_h['Tiempo de Atención'], bins=range(0, int(df['Tiempo de Atención'].max()) + 30, 30), stat='count', kde=True) 
    plt.title('Frecuencia de Tiempo de Atención en Segundos en Puesto de Atención')
    plt.xlabel('Tiempo de Atención (segundos)')
    plt.ylabel('Frecuencia')
    plt.tight_layout()
    plt.show()

    #FDP para Hora de Arribo de los Clientes atendidos por pantalla tactil

    df_p = df[df['Tipo de Atención'] == 'p']

    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    sns.histplot(df_p['Hour'], bins=range(0, 25, 2), stat='count', kde=True)
    plt.title('Frecuencia de clientes por Hora de Arribo de Pantalla Táctil')
    plt.xlabel('Hora de Arribo')
    plt.ylabel('Frecuencia')
    plt.xticks(range(0, 25, 2))
    plt.grid(axis='y')

    #FDP para Tiempo de Atencion de los Clientes atendidos por pantalla tactil

    plt.subplot(1, 2, 2)
    sns.histplot(df_p['Tiempo de Atención'], bins=range(0, int(df['Tiempo de Atención'].max()) + 30, 30), stat='count', kde=True) 
    plt.title('Frecuencia de Tiempo de Atención en Segundos en Pantalla Táctil')
    plt.xlabel('Tiempo de Atención')
    plt.ylabel('Frecuencia')
    plt.tight_layout()
    plt.show()