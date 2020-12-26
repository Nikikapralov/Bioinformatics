DNA = ''
Protein_to_mRNA_Codons = {'F': ['UUU', 'UUC'], 'L': ['CUU', 'CUC', 'UUA', 'CUA', 'UUG', 'CUG'], 'I': ['AUU', 'AUC', 'AUA'], 'V': ['GUU', 'GUC', 'GUA', 'GUG'], 'M': ['AUG'], 'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 'P': ['CCU', 'CCC', 'CCA', 'CCG'], 'T': ['ACU', 'ACC', 'ACA', 'ACG'], 'A': ['GCU', 'GCC', 'GCA', 'GCG'], 'Y': ['UAU', 'UAC'], 'H': ['CAU', 'CAC'], 'N': ['AAU', 'AAC'], 'D': ['GAU', 'GAC'], 'Stop': ['UAA', 'UAG', 'UGA'], 'Q': ['CAA', 'CAG'], 'K': ['AAA', 'AAG'], 'E': ['GAA', 'GAG'], 'C': ['UGU', 'UGC'], 'R': ['CGU', 'CGC', 'CGA', 'AGA', 'CGG', 'AGG'], 'G': ['GGU', 'GGC', 'GGA', 'GGG'], 'W': ['UGG']}
dna_no_introns = ''
introns = []
counter = -1
index = 0
intron_indexes = []
RNA_codons = []
base_number = 0
codon = ''
final_protein = ''
with open('Rosalind_rna.txt', 'r') as file:
    data = file.read().split('\n')
    for line in data:
        if line == '':
            continue
        if 'Rosalind' not in line and counter < 1:
            DNA += line
        elif 'Rosalind' in line and counter < 1:
            counter += 1
        elif 'Rosalind' not in line and counter >= 1:
            introns.append(line)
DNA_1 = DNA
for intron in introns:
    index = DNA.find(intron, index)
    intron_indexes.append(index)
    index += len(intron)
for intron_1 in introns:
    result = DNA_1.split(intron_1)
    DNA_1 = ''.join(result)
RNA = DNA_1.replace('T', 'U')
for base in RNA:
    if base_number < 3:
        codon += base
        base_number += 1
        if base_number == 3:
            base_number = 0
            RNA_codons.append(codon)
            codon = ''
        else:
            continue
for codon_1 in RNA_codons:
    for key, value in Protein_to_mRNA_Codons.items():
        if codon_1 in value and key != "Stop":
            final_protein += key
print(final_protein)
