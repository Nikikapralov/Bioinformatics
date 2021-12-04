import time
genome = ""
with open("Vibrio_cholerae.txt") as file:
    for line in file:
        genome += line
genome = "GACGATATACGACGATA"
pattern = input()
indexes = []
start = 0
while True:
    try:
        result = genome.index(pattern, start + 1, len(genome))
    except ValueError:
        break
    indexes.append(str(result))
    start = result
print(" ".join(indexes))