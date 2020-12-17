DNA_string = input()
Amount_A = 0
Amount_T = 0
Amount_G = 0
Amount_C = 0
for char in DNA_string:
    if char == 'A':
        Amount_A += 1
    elif char == 'T':
        Amount_T += 1
    elif char == 'G':
        Amount_G += 1
    elif char == 'C':
        Amount_C += 1
print(f'{Amount_A} {Amount_C} {Amount_G} {Amount_T}')