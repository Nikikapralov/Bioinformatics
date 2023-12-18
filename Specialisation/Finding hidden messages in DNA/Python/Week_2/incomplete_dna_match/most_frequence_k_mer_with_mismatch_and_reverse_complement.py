from Week_1.reverse_compliment.reverse_compliment_problem import get_reverse_complement
from Week_2.incomplete_dna_match.dna_neighbourhood import neighbourhood_with_mismatch
import os
"""
Here we want to find the count of all k-mers and their mutations in one strand.
As we know, we have the possibility of having reverse complements of some k-mers and
finding a high amount of k-mers and their reverse complements if very unusual and therefor
- very interesting.

What we do is we find the count of each k-mer and its mutations in the strand, but we also
find the count of each k-mer reverse complement and its mutations in the strand.
"""

def most_frequent_k_mer_with_mismatch_and_reverse_complement(data, k_mer_length, mismatch):
    frequency_map = {}
    data_length = len(data)
    # Rolling window. For each k-mer.
    for i in range(data_length - k_mer_length):
        pattern = data[i:i + k_mer_length]
        reverse_complemented_pattern = get_reverse_complement(pattern) # Reverse complement of each k-mer
        # Get the neighbourhood of each k-mer, meaning all possibilities of ATGC with a tolerable hamming distance.

        neighbourhood_normal = neighbourhood_with_mismatch(pattern, mismatch)
        # Loop through the neighbourhood and if already found (potential mutation already encountered, increment its
        # counter.
        for neighbour in neighbourhood_normal:
            if neighbour not in frequency_map:
                frequency_map[neighbour] = 1
            else:
                frequency_map[neighbour] += 1

        neighbourhood_reverse_complemented = neighbourhood_with_mismatch(reverse_complemented_pattern, mismatch)
        for neighbour in neighbourhood_reverse_complemented:
            if neighbour not in frequency_map:
                frequency_map[neighbour] = 1
            else:
                frequency_map[neighbour] += 1

    # Find the k-mers with the highest count.
    sorted_k_mers = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)
    most_frequent_k_mers_with_mismatch = []
    try:
        highest_number_count = sorted_k_mers[0][1]
    except IndexError:
        return most_frequent_k_mers_with_mismatch

    for k_mer, count in sorted_k_mers:
        if count == highest_number_count:
            most_frequent_k_mers_with_mismatch.append(k_mer)
        else:
            break
    return most_frequent_k_mers_with_mismatch
