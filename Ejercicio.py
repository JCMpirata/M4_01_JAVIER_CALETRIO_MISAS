import pandas as pd

#1. Mostrar los 5 primeros registros de cada tabla
titulos = pd.read_csv('imdb_titulos.csv')
print(titulos.head(5))
elenco = pd.read_csv('imdb_elenco.csv')
print(elenco.head(5))

# 2. ¿Cuántos registros hay en cada tabla?
numero_registros_titulos = len(titulos.axes[0])
print("Numero de registros en titulos: ", numero_registros_titulos)
numero_registros_elenco = len(elenco.axes[0])
print("Numero de registros en elenco: ", numero_registros_elenco)

# 3. Mostrar las 5 películas mas antiguas
titulos.nsmallest(5, 'year')

# 4. Mostrar numero de peliculas que tienen "Dracula" en el titulo
print(titulos[titulos.title.str.contains("Dracula")].count())
print(elenco[elenco.title.str.contains("Dracula")].count())

# 5. Mostrar los 10 titulos mas comunes
print(titulos.title.value_counts().head(10))
print(elenco.title.value_counts().head(10))

# 6. Mostrar cual fue la primera pelicula hecha llamada "Romeo and Juliet"
Romeo_Julieta = titulos[titulos.title == "Romeo and Juliet"].sort_values(by='year').head(1)
print(Romeo_Julieta.nsmallest(1, 'year'))
Romeo_y_Julieta = elenco[elenco.title == "Romeo and Juliet"].sort_values(by='year').head(1)
print(Romeo_y_Julieta.nsmallest(1, 'year'))

# 7. Listar todas las peliculas que contengan "Exorcist" de la mas antigua a la mas nueva
Exorcist = titulos[titulos.title.str.contains("Exorcist")].sort_values(by='year')
print(Exorcist)
Exorcista = elenco[elenco.title.str.contains("Exorcist")].sort_values(by='year')
print(Exorcista)

# 8. Mostrar cuantas peliculas fueron hechas en 1950
print(titulos[titulos.year == 1950].count())
print(elenco[elenco.year == 1950].count())










