# -*- coding: utf-8 -*-
"""Mapas de calor y boxplots.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_nAjWT-NzXk1yfEqhmG9Yc-j92dT4oLL
"""

#Francisco Javier Romo Juárez - A01643189
#Cargamos las librerías que vamos a utilizar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("clientes-centro-comercial.csv") #Leemos el archivo que contiene la base de datos que vamos a utilizar

print(df.head()) #Imprimos la tabla de datos

print(df.describe()) #Vemos estadísticas de la tabla

print(df.groupby(['Genero'])) #Data frame es columna Genero

#Hacemos una tabla que corresponde a la cantidad de hombres y la cantidad de mujeres que hay
fig = plt.figure()

sns.countplot(data = df, y = 'Genero')

plt.xlabel("Cantidad")
plt.ylabel("Hombres/Mujeres")
plt.title("Cantidad de Hombres/Mujeres")

#Hacemos un histograma que relaciona los Ingresos anuales y lo separa por generos
fig = plt.figure()
sns.histplot(data=df, x = 'Ingresos Anuales (k$)', hue = 'Genero', bins=20, kde=True)

plt.xlabel("Genero")
plt.ylabel("Ingresos Anuales (k$)")
plt.title("Histograma de Ingresos Anuales (k$) por Genero")

#Hacemos un diagrama de dispersión Usando como ejes, Ingresos Anuales, Puntos en compras y lo dividimos por generos
fig = plt.figure()
sns.scatterplot(data=df, x = 'Ingresos Anuales (k$)', y = 'Puntos en compras (1-100)', hue = 'Genero')

#df['Petal.Length'].hist()

plt.xlabel("Ingresos Anuales (k$)")
plt.ylabel("Puntos en compras (1-100)")
plt.title("Scatter de Clientes")

#Hacmos varios diagramas para ver las relaciones que existen entre las distintas variables
sns.pairplot(data=df, hue = 'Genero')

plt.title("Clientes")

#Hacemos una tabla de correlación entre las variables antes usadas para ver si estan relacionadas de cierta manera, no significa que esten causadas entre si
corr = df.corr()
sns.heatmap(data = corr, vmin =-1, vmax = 1, cmap = "gnuplot", annot=True)

#Hacemos un boxplot de Ingresos Anuales
fig = plt.figure(figsize = (9,5))

sns.boxplot(data = df,x = "Ingresos Anuales (k$)")

# Linea horizontal indica mediana
# Limites de caja indican percentiles
# Bigotes indica minimo y max estadistico

#Hacemos un boxplot de Puntos de Compras
fig = plt.figure(figsize = (9,5))

sns.boxplot(data = df,x = "Puntos en compras (1-100)")

#Hacemos un boxplot de Puntos de Compras pero dividido en Genero
fig = plt.figure(figsize = (9,5))

sns.boxplot(data = df,x = "Puntos en compras (1-100)", y = "Genero")

#Hacemos un boxplot de Edad dividido en Genero
fig = plt.figure(figsize = (9,5))

sns.boxplot(data = df,y = "Edad", x = "Genero")

#¿Hay alguna variable que no aporta información?

#R = Si, en este caso la variable que no aporta información sería el ID del cliente ya que solo es un identificador para quien este leyendo el sistema pueda llegar a un cliente en específico.

#Si tuvieras que eliminar variables, ¿cuáles quitarías y por qué?

#R = Como había mencionado antes, quitaría como variable el ID por que no representa a nivel estadístico algo que nos diga alguna tendencia de los datos, solo los enumera y eso apesar que en el mapa de calor salga en una caso con una correlación cercana a 1.

#¿Existen variables que tengan datos extraños?

#R = Si, ingresos anuales tiene un dato atípico, esto lo podemos ver en su boxplot afuera del rango estadístico en la parte derecha, representando que un cliente tiene Ingresos anuales demasiado superiores a el resto, por lo que no va ayudar a detectar tendencias.

#Si comparas las variables, ¿todas están en rangos similares? ¿Crees que esto afecte?

#R = No, además de que tenemos ID que esta en un rango del tamaño de datos, también tenemos un dato cualitativo que es genero. En realidad el rango no afecta mucho a los datos en este caso ya que los otros datos que si son más significativos, sí tinenn un rango similar.

#¿Puedes encontrar grupos qué se parezcan? ¿Qué grupos son estos?

#R = Sí hay un grupo que se parece con otro siendo una tabla de dispersión con ejes Id clientes y Puntos de compra, y otra con ejes Ingresos Anuales y Puntos de compra. Con esto podemos ver un patro de una X en el que se forman 5 grupos que sí son de interés.