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

# 9. Mostrar cuantas peliculas fueron hechas de 1950 a 1959
print(titulos[(titulos.year >= 1950) & (titulos.year <= 1959)].count())
print(elenco[(elenco.year >= 1950) & (elenco.year <= 1959)].count())

# 10. Mostrar todos los roles que hubo en la pelicula "The Godfather". Tambien mostrar el numero total de coindicencias
roles_titulos1 = titulos[titulos.title == "The Godfather"]
print(roles_titulos1)
roles_titulos2 = roles_titulos1.iloc[:,4]
print(roles_titulos2)
roles_titulos3 = roles_titulos2.value_counts()
print(roles_titulos3)

roles_elenco1 = elenco[elenco.title == "The Godfather"]
print(roles_elenco1)
roles_elenco2 = roles_elenco1.iloc[:,3]
print(roles_elenco2)
roles_elenco3 = roles_elenco2.value_counts()
print(roles_elenco3)

# 11. Mostrar el elenco ordenado por la clasificacion "n" de la pelicula "Dracula" de 1958
clasificacion = elenco[(elenco.title == "Dracula") & (elenco.year == 1958)].sort_values(by='n')
print(clasificacion)

# 12. Mostrar cuantos papeles de "Bruce Wayne" han sido hechos en la historia de las peliculas
print(titulos[tiulos.character == "Bruce Wayne"].count())
print(elenco[elenco.character == "Bruce Wayne"].count())

# 13. Mostrar cuantos papeles ha hecho "Robert De Niro" a lo largo de su carrera
print(titulos[titulos.name == "Robert De Niro"].count())
print(elenco[elenco.name == "Robert De Niro"].count())













