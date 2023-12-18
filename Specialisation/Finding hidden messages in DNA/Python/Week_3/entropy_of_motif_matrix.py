"""
Let us compute the entropy of a motif matrix.
For example the matrix:
A T
A T
A C
A C

has sum values equal to 1
A 1 0.5
T 0 0
C 0 0.5
G 0 0

etc for the other

Then we compute the total entropy of the string like that:
-Sum(entry * log2entry) Entry being 1 for A, 0 for T etc, going COLUMN by column.
This way, we get the entropy of each column.
Very conserved = low entropy (low chaos)
Very diversed = high entropy (high chaos)

Entropy of a matrix - sum of entropies of its columns.

In the end, this is a way to compare how close to each other different strings and parts of them are.
"""
import math

dna_strings = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC",
]


def find_entropy_of_dna_matrix(dna_matrix: list[str]) -> float:
    """
    Find the entropy of a dna matrix. DNA strings must be of equal length.
    """
    bases = {"A", "T", "C", "G"}
    total_dna_strings = len(dna_matrix)
    total_base_count = len(dna_matrix[0])
    column_entropy = []  # The entropy for each column
    single_contribute = 1 / total_dna_strings  # To get how much each base contributes. If 10 strings, each base contributes 0.1
    for base_column_index in range(0, total_base_count):
        dna_base_distribution_matrix = {base: 0.0 for base in bases}
        entropy = 0  # Calculate the entropy of each column
        for row in dna_matrix:
            base = row[base_column_index]
            dna_base_distribution_matrix[base] += single_contribute
        for entry, value in dna_base_distribution_matrix.items():
            dna_base_distribution_matrix[entry] = round(value, 2)  # Round the values at the end, otherwise wont sum to 1.
            value_for_entropy = dna_base_distribution_matrix[entry]
            if value == 0:  # 0LOG20 is undefined, but in our case we just skip.
                continue
            entropy += -(value_for_entropy * math.log(value_for_entropy, 2)) # This is how we compute the entropy of a column
        print(dna_base_distribution_matrix)
        column_entropy.append(entropy)  # The entropy of the column has to be negative
    print(column_entropy)
    return sum(column_entropy)  # The entropy of a matrix is the sum of the entropy of all columns

print(find_entropy_of_dna_matrix(dna_strings))



def countMotifPercent(motifs):
    count = {}
    columns = []
    for i in range(len(motifs[0])):
        columns.append([motif[i] for motif in motifs])
    for i in range(len(columns)):
        count[i] = {'A': columns[i].count('A')/len(columns[i]), 'C': columns[i].count('C')/len(columns[i]), 'G': columns[i].count('G')/len(columns[i]), 'T': columns[i].count('T')/len(columns[i])}
    [print(count[entry]) for entry in count]
    return count


def motifEntropy(motifs):
    entropy = 0
    percents = countMotifPercent(motifs)
    for i in range(len(percents)):
        for nucleotide in percents[i]:
            if percents[i][nucleotide] != 0:
                entropy += percents[i][nucleotide] * math.log2(percents[i][nucleotide])
    return -entropy
