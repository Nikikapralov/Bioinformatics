strand_1 = input()
strand_2 = input()
mutations = 0
for index, base in enumerate(strand_1):
    if base != strand_2[index]:
        mutations += 1
print(mutations)
