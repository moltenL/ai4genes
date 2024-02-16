import pandas as pd
import requests
import csv
import json

# activate virtual env - .venv\Scripts\activate.bat

UNIQUE_VARIATIONS = {'stop_gained', 'protein_altering_variant', 'missense_variant'}

# Open and read file
file = open("gwas-association-downloaded_2024-02-07-EFO_0009443-withChildTraits_Breast-Cancer.tsv")
tsv_file = csv.reader(file, delimiter="\t")
matching_data = []


# Useful table columns and what they contain, only applie to GWAS catalog
# index 24 = CONTEXT
# index 14 = MAPPED_GENE
# index 21 = SNPS

# Reduce file to only usable types of mutations
for line in tsv_file:
    if line[24] in UNIQUE_VARIATIONS:
        matching_data.append(line)
        # print(line[14])
        # print(line[21])

# Get variation and convert to usable format
request = requests.get("https://clinicaltables.nlm.nih.gov/api/snps/v3/search", params={'terms': 'rs16991615', 'maxList': 20})
res = json.loads(request.text)

print(res[3])



# print(matching_data)




# data = pd.read_csv('gwas-association-downloaded_2024-02-07-EFO_0009443-withChildTraits_Breast-Cancer.tsv', sep='\t', encoding='latin-1')

# keys = list(data.keys())

# variations = data['CONTEXT']

# for item in data:
#     print(item)
    # if item['CONTEXT'] in unique_variations:
    #     matching_data.append(item)

# print(data['CONTEXT'])