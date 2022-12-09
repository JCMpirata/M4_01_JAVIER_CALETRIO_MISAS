import pandas as pd

#1. Mostrar los 5 primeros registros de cada tabla
titulos = pd.read_csv('imdb_titulos.csv')
titulos.head(5)
elenco = pd.read_csv('imdb_elenco.csv')
elenco.head(5)

# 2. ¿Cuántos registros hay en cada tabla?
numero_registros_titulos = len(titulos.axes[0])
print("Numero de registros en titulos: ", numero_registros_titulos)
numero_registros_elenco = len(elenco.axes[0])
print("Numero de registros en elenco: ", numero_registros_elenco)

# 3. Mostrar las 5 películas mas antiguas
titulos.nsmallest(5, 'year')

# 4. Mostrar numero de peliculas que tienen "Dracula" en el titulo
titulos[titulos.title.str.contains("Dracula")].count()
elenco[elenco.title.str.contains("Dracula")].count()



