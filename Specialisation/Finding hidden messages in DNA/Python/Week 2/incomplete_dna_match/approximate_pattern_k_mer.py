import os
from hamming_distance import get_hamming_distance
path = os.path.join(os.curdir, "dataset.txt")

k_mer_match = "CCGGCGAGA"
maximal_error_rate = 5

"""
We can search for a specific k-mer, but we can also allow for a k-mer to be incomplete and have some mistakes,
since the Dna A will bind to a somewhat incomplete k-mer anyway.
We can get the starting positions of all k-mers in the DNA that have a tolerable Hamming Distance.
"""

def get_starting_positions_of_approximate_pattern_k_mer(data, k_mer_match, maximal_error_rate):
    results = []
    k_mer_length = len(k_mer_match)
    maximal_index_point = len(data) - k_mer_length + 1
    for i in range(0, maximal_index_point):
        k_mer = data[i:i+k_mer_length]
        if get_hamming_distance(k_mer, k_mer_match) <= maximal_error_rate:
            print(k_mer, k_mer_match, i)
            results.append(str(i))
    return results

