import sys
highest_percentage = -sys.maxsize
rosalind = []
dna = []
final_dna = []
index = -1
rosalind_dna = 0
index1 = -1
with open('rosalind_gc.txt', 'r') as file:
    data = file.read()
    split_data_1 = data.split('\n')
    for x in split_data_1:
        if 'Rosalind' in x:
            rosalind.append(x)
        else:
            dna.append(x)
    for x in rosalind:
        final_dna.append('')
    for x in split_data_1:
        if 'Rosalind' in x:
            index += 1
        else:
            final_dna[index] += x

    for x in final_dna:
        count_G = x.count('G')
        count_C = x.count('C')
        GC_sum = count_C + count_G
        length_of_dna = len(x)
        percentage = GC_sum / length_of_dna
        index1 += 1
        if percentage > highest_percentage:
            highest_percentage = percentage
            rosalind_dna_index = index1
    for x in rosalind[rosalind_dna_index]:
        final = rosalind[rosalind_dna_index].split('>')
    for x in final:
        if x == '':
            final.remove(x)
    for x in range(len(final)):
        print(final[x])
    print(f'{highest_percentage * 100:.6f}')


