import pandas as pd
from variation import get_variation_info

# Useful table columns and what they contain, only applies to GWAS catalog
# index 24 = CONTEXT
# index 14 = MAPPED_GENE
# index 21 = SNPS

active_statuses = ['missense_variant','stop_gained', 'nonsense', 'frameshift']

def sort(file_in, file_out):

    # Read the .tsv or .csv file into a pandas DataFrame
    if file_in.endswith('.tsv'):
        df = pd.read_csv(file_in, sep='\t', encoding='ISO-8859-1')
    else:
        df = pd.read_csv(file_in, encoding='ISO-8859-1')

    df_sorted = df['CONTEXT'].isin(active_statuses)
    df = df[df_sorted]
    df.reset_index(drop=True, inplace=True)
    
    df_change_values = []
    df_change_column = pd.DataFrame(columns=['AACHANGE'])

    # Finds AAchange column or creates AAchange column using API function
    if 'AACHANGE' not in df.columns.map(str.upper) and 'CHANGE' not in df.columns.map(str.upper):

        for row in df['SNPS']:
           df_change_values.append(get_variation_info(row))

    else:

        # Filter the DataFrame to get rows where 'AACHANGE' or 'CHANGE' has NaN values
        if 'AACHANGE' in df.columns.map(str.upper):
            for index, rows in df[['SNPS', 'AACHANGE']].iterrows():
                if pd.isna(rows['AACHANGE']):
                    df_change_values.append(get_variation_info(rows['SNPS']))

                else:
                    df_change_values.append(rows['CHANGE'])

            df = df.drop('AACHANGE', axis=1)

        else:
            for index, rows in df[['SNPS', 'CHANGE']].iterrows():
                if pd.isna(rows['CHANGE']):
                    df_change_values.append(get_variation_info(rows['SNPS']))

                else:
                    df_change_values.append(rows['CHANGE'])
            df = df.drop('CHANGE', axis=1)

    df_change_column['AACHANGE'] = df_change_values
    df = df.join(df_change_column)
    
    if file_in.endswith('.tsv'):
        df.to_csv(file_out, sep='\t', encoding='ISO-8859-1')
        print("Sort complete")

    else:
        df.to_csv(file_out, encoding='ISO-8859-1')
        print("Sort complete")
    return df

sort(
    "Data/gwas-association-downloaded_2024-02-07-EFO_0009443-withChildTraits_Breast-Cancer.tsv",
    "Data/output.txt"
    )