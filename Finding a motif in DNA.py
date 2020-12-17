dna_string = input()
potential_repeat = input()
start = 0
while True:
    start = dna_string.find(potential_repeat, start)
    if start == -1:
        break
    result = start + 1
    print(result, end=' ')
    start += 1










