import pandas as pd
from variation import get_variation_info

# Useful table columns and what they contain, only applies to GWAS catalog
# index 24 = CONTEXT
# index 14 = MAPPED_GENE
# index 21 = SNPS

active_statuses = ['missense_variant','stop_gained', 'nonsense', 'frameshift']

def sort(file):

    # Read the .tsv or .csv file into a pandas DataFrame
    if file.endswith('.tsv'):
        df = pd.read_csv(file, sep='\t', encoding='ISO-8859-1')
    else:
        df = pd.read_csv(file, encoding='ISO-8859-1')

    # Finds AAchange column or creates AAchange column
    if 'AAchange' not in df.columns:
        df_change_values = []
        df_change_column = pd.DataFrame(columns=['AAchange'])

        for row in df['SNPS']:
            df_change_values.append(get_variation_info(row))

        df_change_column['AAchange'] = df_change_values

        df.join(df_change_column)

    mask = df['CONTEXT'].isin(active_statuses)
    
    return df[mask]