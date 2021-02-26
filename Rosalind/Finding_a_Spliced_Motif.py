dna = ''
counter = -1
dna_subseq = ''
dna_subseq_indexes = []

with open('Rosalind_dna.txt', 'r') as file:
    data = file.read().split('\n')
    for line in data:
        if line == '':
            continue
        if 'Rosalind' in line and counter < 1:
            counter += 1
            continue
        elif 'Rosalind' not in line and counter < 1:
            dna += line
        elif 'Rosalind' not in line and counter >= 1:
            dna_subseq += line

start = 0

for index, value in enumerate(dna_subseq):
    if len(dna_subseq_indexes) == len(dna_subseq):
        break
    for base_index in range(start, len(dna)):
        if value == dna[base_index]:
            start = base_index
            if base_index + 1 in dna_subseq_indexes:
                start += 1
                continue
            dna_subseq_indexes.append(base_index + 1)
            break
str_dna_subseq_indexes = map(lambda x: str(x), dna_subseq_indexes)

print(' '.join(str_dna_subseq_indexes))