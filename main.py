import pandas as pd
from program import CountValues

# Charger les données depuis un fichier CSV
df = pd.read_csv('data.csv')

# Créer une instance de CountValues
count_values = CountValues(df)

# Compter les valeurs uniques par bloc dans la colonne 3
result = count_values.count_values_by_block('col3')

# Afficher le résultat
print(result)