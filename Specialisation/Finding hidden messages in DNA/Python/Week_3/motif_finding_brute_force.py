import os

from Week_2.incomplete_dna_match.dna_neighbourhood import neighbourhood_with_mismatch
from Week_2.incomplete_dna_match.approximate_pattern_k_mer import get_starting_positions_of_approximate_pattern_k_mer
from utils.utils import get_data

"""
Find all k-mers that appear in all strings with a maximum of d hamming distance mismatch.
The brute force method relies on the assumption that a k-mer with most d mismatch will appear
at least once in the first string. So by that logic, if we generate all k-mers with most d mismatches from the 
first string (neighbourhood), then check for each such k-mer if it appears in all strings, we will find our desired
k-mer appearing in all strings with at most d mismatches.
"""
path = os.path.join(os.curdir, "dataset.txt")
data = get_data(path)
dna_strands = data.split(" ")
k_mer_length = 5
mismatch = 1

def motif_finder_brute_force(dna_strands, k_mer_length, mismatch):
    results = set()
    first_strand = dna_strands[0]
    maximum_index = len(first_strand) - k_mer_length
    for i in range(maximum_index):
        pattern = first_strand[i:i + k_mer_length]
        pattern_neighbourhood = neighbourhood_with_mismatch(pattern, mismatch)
        # Now for each pattern in the neighbourhood, we have to check if it appears in all strings with at most d mismatches.
        # If it does, we add it to results, else we continue.
        for pattern_neighbour in pattern_neighbourhood:
            is_in_all = True
            for strand in dna_strands:
                # Check if the neighbour appears in the strand with at most d mismatch.
                starting_positions = get_starting_positions_of_approximate_pattern_k_mer(strand, pattern_neighbour, mismatch)
                if not starting_positions:
                    is_in_all = False
                    break

            if is_in_all: # If it appears in all, simply add it to results.
                results.add(pattern_neighbour)

    return results

result = motif_finder_brute_force(dna_strands, k_mer_length, mismatch)
print(" ".join(result))