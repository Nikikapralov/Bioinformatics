"""
This is a faster way to find the string by which the entropy of the matrix is the lowest.
We concatenate all the strings, then we go k-mer by k-mer using the rolling window technique.
Afterwards, for each k-mer, we go and find the score. The one with the lowest score is our k-mer.
"""
import os
import sys
from Week_2.incomplete_dna_match.hamming_distance import get_hamming_distance

from utils.utils import get_data

path = os.path.join(os.curdir, "dataset.txt")
data = get_data(path)
data = data.split(" ")
length_k = 6

def median_string(dna_strings_matrix, k_mer_length):
    one_big_dna = "".join(dna_strings_matrix) # Instead of looping through permutations,
    # just loop through existing k-mers of all strings joined together.
    maximum_index = len(one_big_dna) - k_mer_length
    k_mer_set = set()
    current_distance = sys.maxsize
    k_mer_with_lowest_score = None
    for index in range(maximum_index):
        k_mer = one_big_dna[index:index+k_mer_length]
        if k_mer not in k_mer_set:
            k_mer_set.add(k_mer)
            k_mer_distance = compute_distance(k_mer, dna_strings_matrix, k_mer_length)
            if current_distance > k_mer_distance:
                current_distance = k_mer_distance
                k_mer_with_lowest_score = k_mer
    return k_mer_with_lowest_score


def compute_distance(k_mer, dna_strings_matrix, k_mer_length):
    total_distance = 0
    for dna_string in dna_strings_matrix:
        maximum_index = len(dna_string) - k_mer_length
        lowest_hamming_distance = sys.maxsize
        for index in range(maximum_index):
            potential_match = dna_string[index:index + k_mer_length]
            current_hamming_distance = get_hamming_distance(potential_match, k_mer)
            if current_hamming_distance < lowest_hamming_distance:
                lowest_hamming_distance = current_hamming_distance
        total_distance += lowest_hamming_distance
    return total_distance



print(median_string(data, length_k))

