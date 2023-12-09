dna_string = input()
compliments = {"A": "T", "T": "A", "G": "C", "C": "G"}
compliment_string = ""
for base in dna_string:
    compliment_string += compliments[base]
result = compliment_string[::-1]
print(result)