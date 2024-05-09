import requests

def get_variation_info(rsID):
    '''Given an rsID return a list of all the amino acid changes'''
    ID = rsID[2:]
    # ClinVar API endpoint for variation data
    url = f"https://api.ncbi.nlm.nih.gov/variation/v0/refsnp/{ID}"

    # Perform GET request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()

        # Extract relevant information from the response
        variations = []
        if 'primary_snapshot_data' in data:
            for allele in data['primary_snapshot_data']['placements_with_allele']:
                for allele_info in allele['alleles']:
                    actual_info = allele_info['allele']['spdi']
                    if actual_info['seq_id'][0:2] == 'NP' or actual_info['seq_id'][0:2] == 'XP':
                        # position + 1 because all of the positions listed are off by 1
                        AAchange = actual_info['deleted_sequence']+str(actual_info['position']+1)+actual_info['inserted_sequence']
                        variations.append(AAchange)
        return list(set(variations))
    else:
        print("Failed to fetch variation information.")
        return None