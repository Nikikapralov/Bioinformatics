"""
Find the most probable motif that can be generated from the string according to the given profile.
The profile is created from the concencus string, the one supposedly found most often in the dna strands.
We go k-mer by k-mer and we see how close our k-mer is to the probability profile of the string. If it is very close,
we will receive a higher probability value. If not - a lower probability value.
"""
import sys

import numpy
data = "TTGAGACTAATAGAACGAATAGTGGTGTTGCCTTACACCGCTATTGGAGCTCAGTACGTAATCGAAGGCCACTGCTTGAGCACAGGCGGGTATCGGATAGTGTCACCCCGAATTCATTAATCGATAAAGACCCGGGTATGGGTTGTTCCGCTCGCATTTAATGTGTCTTAATGCCTATAGACACACTTACACCCGAGAGACTTAAGGTTAATTAAGTGGTATTAGATCACACCGCCCACACGGATGCACTCTCCTCGCGGATGACGCCCGGAACTCTTTCTCACCACCGACCGTTCCGAGCGGTCGCGCCTCGAATTCTTAAATTCGTATGGGGCAGTCGACGGATCATTTCTAACAACTAGCGTACCCCTTAGAGCATGTGATGCGCCCAGCGGCTAAGGTACATGATGAATGCTGTTTAACCGCGGGGATCTGATACTTGCCGCTTAGTTAGGTTGGACTTGTTCGGTTGGTGCTCGATTCTCCTGAGATAGAGCCTTGTACTCCGTGTTTAATCCAGGACCGTCAAGGGTTGCGCGACCTGTCTATGGCTCGTTGCTAGTGCATCCACTAGTTCGTTGGGGGTTATACGAGTCTCGGAAAGTTCAGCATTTAAACTCGGGGATCGTGATCAGTCACGAAACCAATGGGGAATGTCCGAAAGGATCTCGTATCGACATTTTCCCTTGCCAATCATTGCCCTTTGGGCCCGTCATCTCTTTTCAGCACAGCCGTACCTGTTTCTACCATACCCATGGTACCGTAGTCTGATGTAAATAAACGGCCTATACGTCGACAACAACTGGGCGTGGTAGGTTTCTTGTCACCTGTTGTGGGTCCCCTATATTTAAATGTAAGCCGGTCTAACTAGGTACTTATAAGTAAAGGGTGGTCCGTGGAATTCGTCTACCGAGCCAGGTCGTTTACTGTTGCTGTTGCCGATCCTTAATACTCGATAGGCGCCGAACCATTTGAGGCTCCTAATGGTAAGACATGTTTT"
k_mer_length = 13
matrix = "0.342 0.316 0.237 0.237 0.211 0.263 0.329 0.263 0.171 0.263 0.303 0.316 0.224 \
0.276 0.211 0.211 0.25 0.237 0.224 0.184 0.329 0.329 0.316 0.158 0.197 0.355 \
0.171 0.211 0.25 0.25 0.184 0.224 0.224 0.25 0.197 0.211 0.263 0.211 0.211 \
0.211 0.263 0.303 0.263 0.368 0.289 0.263 0.158 0.303 0.211 0.276 0.276 0.211"
matrix = matrix.split(" ")
matrix = [matrix[index:index + k_mer_length] for index in range(0, len(matrix), k_mer_length)]

table = {
    "A": None,
    "C": None,
    "G": None,
    "T": None,
}

for index, key in enumerate(table):
    table[key] = matrix[index]

def get_most_probable_motif_according_to_probability_matrix(data, k_mer_length, table):
    """
    Get the most probable motif according to the sum of the probabilities in the matrix.
    First, choose a k_mer by doing a rolling window. Next, go through each base of the k_mer
    and adds its probability to the total probability for said k_mer. Keep the k_mer with the
    highest probability as most probable. Why is this version bad though? Well, one mismatch will
    result in 0 probability, causing the whole string to have a result of 0 even if all other bases match
    perfectly. This makes it as bad as the brute force approach, although much faster.
    """

    max_index = len(data) - k_mer_length + 1
    highest_probability_and_k_mer = [None, -sys.maxsize]
    for index in range(0, max_index):
        k_mer = data[index:index+k_mer_length]
        current_probability = 1
        for i, base in enumerate(k_mer):
            current_probability *= float(table[base][i])

        if current_probability > highest_probability_and_k_mer[1]:
            highest_probability_and_k_mer[1] = current_probability
            highest_probability_and_k_mer[0] = k_mer

    return highest_probability_and_k_mer




