def get_reverse_complement(dna_string):
    complements = {"A": "T", "T": "A", "G": "C", "C": "G"}
    complement_string = ""
    for base in dna_string:
        complement_string += complements[base]
    result = complement_string[::-1]
    return result