import pandas as pd

#1. Mostrar los 5 primeros registros de cada tabla
data = pd.read_csv('imdb_titulos.csv', on_bad_lines='skip')
print(data.head(5))










