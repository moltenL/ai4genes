#2 different testing protein sequences for GATA4
example_sequence = ["MFDDFSEGRECVNCGAMSTPLWRRDGTGHYLCNACGLYHKMNGINRPLIKPQRRLSASRRVGLSCANCQTTTTTLWRRNAEGEPVCNACGLYMKLHGVPRPLAMRKEGIQTRKRKPKNLNKSKTPAAPSGSESLPPASGASSNSSNATTSSSEEMRPIKTEPGLSSHYGHSSSVSQTFSVSAMSGHGPSIHPVLSALKLSPQGYASPVSQSPQTSSKQDSWNSLVLADSHGDIITA", "MVDDFSEGRECVNCGAMSTPLWRRDGTGHYLCNACGLYHKMNGINRPLIKPQRRLVPRPLAMRKEGIQTRKRKPKNLNKSKTPAAPSGSESLPPASGASSNSSNATTSSSEEMRPIKTEPGLSSHYGHSSSVSQTFSVSAMSGHGPSIHPVLSALKLSPQGYASPVSQSPQTSSKQDSWNSLVLADSHGDIITA"]
example_mutation = ["D3X", "D3F", "V2E", "Y4E"]

#Returns the mutated protein sequence given possible protein sequences and mutations
#sequence_list - the given protein sequences as a list of strings
#mutation_list - the given mutations for a protein as a list of strings. Ex) D3X = at position 3 replace D with X
def generateMutated(sequence_list, mutation_list):
    #Will store a map of the protein sequences with the original sequence as the key and the values being a list of the edited sequences
    sequences_map = {}
    
    #Iterates through all of the protein sequences in the given list for that protein
    for protein_sequence in sequence_list:
        edited_sequences = []

        #Iterates through the mutations in the mutation list given
        for mutation in mutation_list:
            index_seperated = []
            letters_seperated = []

            #Seperates the digits in the mutation and adds it to the list index_seperated
            #Seperates the letters in the mutation and adds it to the letters_seperated
            for i in mutation:
                if (i.isdigit()):
                    index_seperated.append(i)
                else:
                    letters_seperated.append(i)

            #Joins the digits in index_seperated to an integer and subtracts 1 so it's the aligned index number        
            mutation_index = int("".join(index_seperated)) - 1            

            #Edits the protein sequence according to the mutation
            if(protein_sequence[mutation_index] == letters_seperated[0]):
                edited_sequences.append(protein_sequence[:mutation_index] + letters_seperated[1] + protein_sequence[mutation_index + 1:])
        
        #Adds an entry to sequences_map with the key being the original sequence and the value being a list of the edited sequences
        sequences_map[protein_sequence] = edited_sequences

    return sequences_map

#Calls the example
print(generateMutated(example_sequence, example_mutation))
