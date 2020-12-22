m_rna_string = list(input())
counter = 0
for index, codon in enumerate(m_rna_string):
    if codon != ' ':
        counter += 1
    if counter == 3:
        m_rna_string.insert(index + 1, ' ')
        counter = 0
current_codon = ''
base_count = 0
protein = ''
for base in m_rna_string:
    if base != ' ':
        current_codon += base
        base_count += 1
        if base_count == 3:
            base_count = 0
            if 'UUU' in current_codon:
                protein += 'F'
            elif 'UUC' in current_codon:
                protein += 'F'
            elif 'UUA' in current_codon:
                protein += 'L'
            elif 'UUG' in current_codon:
                protein += 'L'
            elif 'UCU' in current_codon:
                protein += 'S'
            elif 'UCC' in current_codon:
                protein += 'S'
            elif 'UCA' in current_codon:
                protein += 'S'
            elif 'UCG' in current_codon:
                protein += 'S'
            elif 'UAU' in current_codon:
                protein += 'Y'
            elif 'UAC' in current_codon:
                protein += 'Y'
            elif 'UAA' in current_codon:
                break
            elif 'UAG' in current_codon:
                break
            elif 'UGU' in current_codon:
                protein += 'C'
            elif 'UGC' in current_codon:
                protein += 'C'
            elif 'UGA' in current_codon:
                break
            elif 'UGG' in current_codon:
                protein += 'W'
            elif 'CUU' in current_codon:
                protein += 'L'
            elif 'CUC' in current_codon:
                protein += 'L'
            elif 'CUA' in current_codon:
                protein += 'L'
            elif 'CUG' in current_codon:
                protein += 'L'
            elif 'CCU' in current_codon:
                protein += 'P'
            elif 'CCC' in current_codon:
                protein += 'P'
            elif 'CCA' in current_codon:
                protein += 'P'
            elif 'CCG' in current_codon:
                protein += 'P'
            elif 'CAU' in current_codon:
                protein += 'H'
            elif 'CAC' in current_codon:
                protein += 'H'
            elif 'CAA' in current_codon:
                protein += 'Q'
            elif 'CAG' in current_codon:
                protein += 'Q'
            elif 'CGU' in current_codon:
                protein += 'R'
            elif 'CGC' in current_codon:
                protein += 'R'
            elif 'CGA' in current_codon:
                protein += 'R'
            elif 'CGG' in current_codon:
                protein += 'R'
            elif 'AUU' in current_codon:
                protein += 'I'
            elif 'AUC' in current_codon:
                protein += 'I'
            elif 'AUA' in current_codon:
                protein += 'I'
            elif 'AUG' in current_codon:
                protein += 'M'
            elif 'ACU' in current_codon:
                protein += 'T'
            elif 'ACC' in current_codon:
                protein += 'T'
            elif 'ACA' in current_codon:
                protein += 'T'
            elif 'ACG' in current_codon:
                protein += 'T'
            elif 'AAU' in current_codon:
                protein += 'N'
            elif 'AAC' in current_codon:
                protein += 'N'
            elif 'AAA' in current_codon:
                protein += 'K'
            elif 'AAG' in current_codon:
                protein += 'K'
            elif 'AGU' in current_codon:
                protein += 'S'
            elif 'AGC' in current_codon:
                protein += 'S'
            elif 'AGA' in current_codon:
                protein += 'R'
            elif 'AGG' in current_codon:
                protein += 'R'
            elif 'GUU' in current_codon:
                protein += 'V'
            elif 'GUC' in current_codon:
                protein += 'V'
            elif 'GUA' in current_codon:
                protein += 'V'
            elif 'GUG' in current_codon:
                protein += 'V'
            elif 'GCU' in current_codon:
                protein += 'A'
            elif 'GCC' in current_codon:
                protein += 'A'
            elif 'GCA' in current_codon:
                protein += 'A'
            elif 'GCG' in current_codon:
                protein += 'A'
            elif 'GAU' in current_codon:
                protein += 'D'
            elif 'GAC' in current_codon:
                protein += 'D'
            elif 'GAA' in current_codon:
                protein += 'E'
            elif 'GAG' in current_codon:
                protein += 'E'
            elif 'GGU' in current_codon:
                protein += 'G'
            elif 'GGC' in current_codon:
                protein += 'G'
            elif 'GGA' in current_codon:
                protein += 'G'
            elif 'GGG' in current_codon:
                protein += 'G'
            current_codon = ''
print(protein)
