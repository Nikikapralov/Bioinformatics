import sys
sys.setrecursionlimit(2000)
list_of_dna = []
with open('Rosalind_dna.txt', 'r') as file:
    is_first = True
    data = file.read()
    split_data_1 = data.split('\n')
    for x in split_data_1:
        if '>' in x:
            if is_first:
                current_dna = ''
                is_first = False
                continue
            else:
                list_of_dna.append(current_dna)
                current_dna = ''
                continue
        else:
            current_dna += x

dna_length = [len(dna) for dna in list_of_dna]
lowest = min(dna_length)
all_lowest = [dna for dna in list_of_dna if len(dna) == lowest]
list_shared_motifs = []


def shared_motifs(dna, power=50):
    if power > len(dna):
        return
    start = 0
    end = start + power
    while end <= len(dna):
        counter = 0
        current_potential_motif = dna[start:end]
        for item in list_of_dna:
            if current_potential_motif in item:
                counter += 1
                continue
            else:
                break
        if counter == len(list_of_dna):
            list_shared_motifs.append(current_potential_motif)
        start += 1
        end += 1
    power += 1
    shared_motifs(dna, power)


x = 0
for dna in all_lowest:
    print(len(dna))
    print(x)
    shared_motifs(dna)
    x += 1

only_uniques = set(list_shared_motifs)
only_uniques = list(only_uniques)
int_list = [int(len(item)) for item in only_uniques]
if not int_list:
    print('None found')
    exit()
longest_int = max(int_list)
longest = [item for item in only_uniques if len(item) == longest_int]
only_uniques.sort(key=len)
print(only_uniques)
print(*longest)


#len(data) - number(power in our case) + 1 = amount of combinations that we will have


#0123456789 (len(10) - number(2) + 1 = 8 combinations of the first 2 letters 01,12,23,34,45,56,67,78,89)