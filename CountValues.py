class CountValues:
    def __init__(self, df):
        self.df = df
    
    def count_values_by_block(self, column_name):
        # Grouper les données par bloc et compter les valeurs uniques dans la colonne spécifiée
        counts = self.df.groupby(pd.util.hash_pandas_object(self.df)).apply(lambda x: x[column_name].value_counts())
        
        # Convertir la série en dictionnaire
        result = counts.to_dict()
        
        return result