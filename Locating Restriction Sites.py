strand_1 = input()
reverse_strand = strand_1[::-1]
strand_2 = ''
for value in reverse_strand:
    if value == 'A':
        strand_2 += 'T'
    if value == 'T':
        strand_2 += 'A'
    if value == 'C':
        strand_2 += 'G'
    if value == 'G':
        strand_2 += 'C'
# strand_2 is complement
palindromes = []
strand_2_reversed = strand_2[::-1] # for ease of use
for index, base in enumerate(strand_1):
    index = int(index)
    for length in range(4, 13):
        if (index + length) > len(strand_1):
            continue
        current_palindrome_strand_1 = strand_1[index:index + length]
        current_palindrome_strand_2 = strand_2_reversed[index:index + length]
        reverse_current_palindrome_strand_2 = current_palindrome_strand_2[::-1]
        if (current_palindrome_strand_1 == reverse_current_palindrome_strand_2) and (len(current_palindrome_strand_1) in range(4, 13)):
            current_palindrome_list = [index + 1, len(current_palindrome_strand_1), current_palindrome_strand_1]
            palindromes.append(current_palindrome_list)
print(palindromes)
for palindrome in palindromes:
    print(f'{palindrome[0]} {palindrome[1]}')
