protein_string = input()
result = 1
Protein_to_mRNA_count = {'F': 2, 'L': 6, 'I': 3, 'V': 4, 'M': 1, 'S': 6, 'P': 4, 'T': 4, 'A': 4, 'Y': 2, 'H': 2, 'N': 2, 'D': 2, 'Stop': 3, 'Q': 2, 'K': 2, 'E': 2, 'C': 2, 'R': 6, 'G': 4, 'W': 1}
for protein in protein_string:
    for key in Protein_to_mRNA_count:
        if protein == key:
            result *= Protein_to_mRNA_count[key]
            break
result_and_stop_codon = result * 3
final_result = result_and_stop_codon % 1000000
print(final_result)

