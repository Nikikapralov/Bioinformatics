DNA = input()
Reverse_DNA = DNA[::-1]
Reverse_DNA = list(Reverse_DNA)
Complemented_DNA = []
for value in Reverse_DNA:
    if value == 'A':
        Complemented_DNA += 'T'
    if value == 'T':
        Complemented_DNA += 'A'
    if value == 'C':
        Complemented_DNA += 'G'
    if value == 'G':
        Complemented_DNA += 'C'
for x in range(len(Complemented_DNA)):
    print(Complemented_DNA[x], end="")
