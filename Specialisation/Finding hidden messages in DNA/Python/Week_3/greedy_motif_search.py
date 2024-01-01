"""
Greedy Motif search is a heuristics based algorithm that is designed to be fast, but unfortunately isn't very accurate.
How it works:
For each k-mer from the first dna string (like the brute force version),
generate a probability matrix, then see which k-mer in the second string scores best. Add it to the matrix and
repeat for third string. Repeat until all strings are done. Then score the list of best fitting kmer for each DNA string
and go again until all k-mer from first string are exhausted. At the end, return list of motifs with best score.
"""
import sys
from collections import deque
from Week_3.most_probable_motif_according_to_profile import get_most_probable_motif_according_to_probability_matrix

k_mer_length = 12
dna_strings = "TAGGAAATAAGGAAGTCATTGGGTATTGGAATCGATAAAATGGATAAAATAATCCGCAACAAGTCAGTCGCCGCCGACTCGGCATCTGGTTGGCCCGACATCCTGTCATCACCTCTTTCCCCATCGCATAGACGAAAAGCGCCCATCATAACCCGT GAGCTAATCCACCAGGTTGTCTCCAAGGCAGTCTGTTAGTATGAAGGTGGAAGGCACTATTTTAACTGCTGCCCTGTGCAGAACGCCTTATGATTAGTGCGTAGTGCTAGCGTAAGCCGCCCTCATACAGGTCGTCTGGCTATACGATGCTTGCGT AAGACAGTCTGATCCCCGGACATGATTCGCGACCTTTCCGCACAGCCGCCGACAGTCACACCTGGAGTAGCCTTCTAGGCCTAGGGTTAAATTTGCCAACGTGTATACCTGACGAATACATGCCACCCAAAGCAGATGGCTGGCAAAACAATAGAG CCTCGATGGACGACACTAACGTTCGTGTACCAGCGTAATCCCGTAGCTCTAGTGAAACCTCCCGCCTCGTTTCATGAACCATTCGCATGGTAAAGGGCCCATTAGGGTAAGTCAGTCGCCTATACCTGAGAAGGCACGTCTTTCCATGGGAACGGC CGCGCGGGTTGCGGTCTCACATATTGAGTCTTCTTTCTCTATACACGAAGTACCGCCTTAGGCAGTTACTTCAATCAGTGGAAAACCGCTTGCACAAAGGCAGTCGGCGTCCTCCTGAGCCCGTTGAAAATACAGGCCCTATCCGAACAAAATTGC CTATTACCGGGCGTGCTACGAAGCGAGCCTATGGCAGATGACCTTGGGGCGATGAGACGGCAGTACTATCTGAAGGAAGACTAGGTAGTAATGACCATTGCAAATAGCGCCATACGTAGCGCCCTTTCGAGAGAGCTTTGAGTGAAGCCAGTCCAT TTCGCACGGGCTGAGTCAAATGAAACGAGAATGCTGTACTTGTTAATTGCCAAACCCCATTGCCGTTACCTGAAGACAGTCTGAGACGATGACAGTGGTAATTTTGCGATTTACTCCCAGCGGAGGGCCAAAGTGACCGAACGGTTATTTGAGCAA GTTCTATGCGCAAAACAGTACCAAGTGTAGTTGTACAAGTCAGTCAGATGCGGAATTCTCACCTTTCGTATGACCCACTTATGCTTACGACCGTGGGGTGTACAGGAAGTATACTACGTATGGTCGGTACACATCGATTAGAGCGAAACATCAAGT GAACGAACCTCCTAGTGTATAACAAAGAAAAAATCGGATGGTGAGCTCAAGTCAGTCCGGCAACGCTTTAAAAACGATGGCAGCTTCTACTGTTACTTTGCCTAATCGCTTCTGCCAGTTCTTAAGCCGAGACGGCTAGACTCTCCCTTTAAGAAT AACCACGACTTCCTAATGGCAGTCAATTAATCACCGTGAGAGGAACATAAGACAGTCATTCAGCGGAAATGCTAGTAGGTACGGAATTTGGAGTCTAGTTAAATACTACGCACTAATAGTCATTAGACGCGATTGAGGTAATGAAGTATGGTCCTT GTGACCATGGCTGTATTTTTCCCAAAGACAGTCATTGGATACAAGGACAGAAACTCCGTATACCTCAGCCATGCCGGTAGAACGATATTTTCTACTGTGCCACTCGTCGTATGTTCGACCATGCTGCGAATGAAAAAGACTTTGGAACTGGAACAG AAACGAGGTGGCTTCATAGCAACTGTCTGATGTCCCTCCTGCTAATCGAAGGCAGTCGTCGCTCACTGAGTTATCCATCTTAGGATTCACTTTTTGCATTATCCTGAATTATACAACTCTAAGCATGAGACGCGTGAAGAGTCTGACCGCACGATT ACATGTCTTCGGCTAGTGGCGATATACAAAGATCCCCGCCGGCAGTTCCATAATATTGGCAAGTAATGGTTTGAGAGTCAGTTAACCTGAGCAAATAATACTAGACCAAAGACAGTCGCAAGTGGAGAATCACACGTAGGACGGTACTAGTTGTAA AAGGTAGTCGTGGGCACCGGACCGCTTAGTGAAGAGTTTATTTACATTAGAAGGGCTATTTTTAGCACGGATAGACGTTCCTACTACGTATGTACACTGCCGCAGCCAGTGAGTCCCAAGAAGACAGTCAACACATTTTCAGATTTATATATTGTT TGCCTGGCCTCCTTTTGCGCTTCTCTAACGATCGTCCTAGTACGTGGCCTGTCCAATAAGCGGGTATTTACATCTGACCAGATCCGGGGGGGACCCGGTGACGGGTCGTACCTCATGTTAAGAGTTCAATCAGGCGGGGTGTACAAGCCAGTCCTA TGAGGTATCAGAACAAATTCTTTGTAAGGGCGAAATTGGGAATGCTCGATCTCGGAGAGTAAGCCAGTCTTTAGTAGCTAAACCCACCCCACATTAGGACAGGTGATCAACACATTTTAAGACGTTGTGCTATCCTCGTATAGACTGTGCTAGTGG AAGTCAGTCAGCAGCGACAGCTCATGCCTCACTATTACAGCCCTCACAAACCGATTACAGGCTGATACTCGAAAGGGATGCTCGTCTGAATCCTTAACGGAGTGGAGTTGCATTAGGGACGTGATTTCTCTTCATTTTCCTGAATGATGACGCGTG CGAGTCGACATGAGATGTAAAAAGCAAAAGTGTTCGTCTCTAAGAGTCCCATAGATAAGCCTTAGTGGTGGTTGAAAACTAATCAAGTCAGTCTCGGTACTTAAATTCGTGATCGAAATCCAGAATTATACGTAGTGAAATGTAATAAGACCATAC GGAAACAGTAAGCTTTGATCTGGAAAGACAGTCTAATCACAGTAATCTTCGCGTCATCAATTCCGACAGCGCGCCTCCTTACACACTACCGCCATCGAGAAATCTAAGGCACCCTAGCAAAATCTCTGATTCCATGTCTGCCTAAAGCCAGTACTA AGAGCTTTACCGTGATCTCGTGCATGCAAAACTGTTGGGGGGTAGTACTCAGGGTACCGGCTCCAAACATGGGACCTCAATACTCAGCCAGCGCGGTCGAAGCTATGTTAGAGGCAATCAAAGGCAGTCCGTGGCTCTAGAGCGTAGGTCTGGTCG GGGAAGCATCGCATGGTTTGGTGCAGGCAAACTAGACAGCTGAGTGTTTATTCTATCGAACGAGGGCGTGTCACTTACGCTGCGTAAACTTGTCCTTGATTAGGCAGTTCTCAGAAATCTAAGGCAGTCACGCCTTGGTGCGTGTGCGAACAGAGG AAGGCCGGTAGCGAGTCGTAGTTGCAGACCTGGGCGTTACTTGTGTAGGGACAATTACCTAAGACAGTCTCCCCAGAAGGCCTCTTGCTCAAGCGTTCAAGGATCTCACAAGGCGGTCTGACAGAAAGCTAGGTTCGATGGAAATGACAGCTTAAC TCCCACAGGCGCAAGGCAGTCTGGCCAAGTTCCCGCATACGTGCGACATGGACACTATGTTCTTAGCATAACGCAGGCCAGGCACAGCATGTTTGCTAAAGTAACGTTCGGCATCGATTAAGATCGTTGCACCCTATGATCCGAAGTGCAGATCCC ACGTGACCTCTTGTTGCTCCGGCACTATGCTAGCTTAAGACAGTCTGGCGAGTTTGAAATGTCCAACGGTATGAACTAGAGTTAAAAGATCCAAGGAGGTATGAGAAAGTCAGGACCTTATAGTCACCCGGACGTGGTCAACATTCGTGCGAGTAC ATTACCACCGAGAAGTCAGTCTTAATCTGTCAAGATCATTGACTATAATCGTTAAACCTAATCACAGGCTGACTCGCCCCCGAGCGAAGCCGGACTACTCGCTAGCGAGTTAGAAACTCCATGTCTACCGCTCGCCGCTTCACTCGGCCAGAGAGT"
dna_strings = dna_strings.split(" ")
dna_strings = deque(dna_strings)

def greedy_motif_search(k_mer_length, dna_strings):
    first_dna_string = dna_strings.popleft()
    maximum_index = len(first_dna_string) - k_mer_length + 1  # Since range is an exclusive, we need + 1.
    result = []
    history = []
    k_mers_score = sys.maxsize
    for index in range(maximum_index):
        k_mer = first_dna_string[index: index + k_mer_length]
        k_mers = [k_mer]
        probability_matrix = build_probability_matrix(k_mers)  # Build first probability matrix.
        [print(row, value) for row, value in probability_matrix.items()]
        print("-------------------------NEW--------------------------")
        for dna_string in dna_strings:
            most_suitable_kmer = get_most_probable_motif_according_to_probability_matrix(
                dna_string, k_mer_length, probability_matrix
            )  # Most probable k-mer.

            k_mers.append(most_suitable_kmer[0])
            probability_matrix = build_probability_matrix(k_mers)  # Optimize probability matrix.
            [print(row, value) for row, value in probability_matrix.items()]
            print("---------------------------------------------------")
        _, current_score = score_k_mers_and_concencus_string(k_mers)  # Get score of k-mers, should be lowest possible.
        history.append([k_mers, current_score])
        if current_score < k_mers_score:
            k_mers_score = current_score
            result = k_mers
    [print(entry) for entry in history]
    return result

def build_probability_matrix(dna_matrix):
    """
    Build the probability matrix of a set of dna strings.
    """
    bases = {"A", "T", "C", "G"}
    total_dna_strings = len(dna_matrix)
    total_base_count = len(dna_matrix[0])
    single_contribute = 1 / total_dna_strings  # To get how much each base contributes. If 10 strings, each base contributes 0.1
    probability_matrix = []
    for base_column_index in range(0, total_base_count):
        dna_base_distribution_matrix = {base: 0.0 for base in bases}
        for row in dna_matrix:
            base = row[base_column_index]
            dna_base_distribution_matrix[base] += single_contribute
        for entry, value in dna_base_distribution_matrix.items():
            dna_base_distribution_matrix[entry] = round(value, 2)  # Round the values at the end, otherwise wont sum to 1.

        probability_matrix.append(dna_base_distribution_matrix)

    #  Construct the probability matrix in an easy to read way.
    result = {base: [] for base in bases}
    for row in probability_matrix:
        for key, value in row.items():
            result[key].append(value)

    return result

def score_k_mers_and_concencus_string(k_mers):
    [print(k_mer) for k_mer in k_mers]
    score = 0
    concensus_string = ""
    for col_index, value in enumerate(k_mers[0]):
        column = [k_mer[col_index] for k_mer in k_mers]
        set_column = set(column)
        counts = sorted({entry: column.count(entry) for entry in set_column}.items(), key=lambda x: x[1], reverse=True)
        print(counts)
        concensus_string += counts[0][0]
        score += len(k_mers) - counts[0][1]
    return concensus_string, score


print(" ".join(greedy_motif_search(k_mer_length, dna_strings)))  # GTGCGT GTGCGT GCGCCA GTGCCA GCGCCA
