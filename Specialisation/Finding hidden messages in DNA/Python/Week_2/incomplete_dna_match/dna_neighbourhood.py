from Week_2.incomplete_dna_match.hamming_distance import get_hamming_distance

"""
A neighbourhood is defined as all possible version of a k-mer with at most d mismatches.
"""
def neighbourhood(pattern):
    result = set()
    result.add(pattern)
    codons = {"A", "G", "C", "T"}
    for index, value in enumerate(pattern):
        for entry in codons:
            if entry != value:
                to_add = list(pattern)
                to_add[index] = entry
                result.add("".join(to_add))
    return result

def neighbourhood_with_mismatch(pattern, mismatch):
    if mismatch == 0: # If possibility for mismatch is 0, return the same pattern. It cannot change.
        return {pattern}
    if len(pattern) == 1: # If the pattern is just 1 character,
        # then even if it could change, only the bases can be answer.
        return {"A", "T", "C", "G"}
    result = set()
    suffix_pattern = pattern[1:] # Next pattern, until len(pattern) is 1;
    suffix_neighbours = neighbourhood_with_mismatch(suffix_pattern, mismatch) # Recurse inside tree.

    for text in suffix_neighbours: # Suffix neighbours will at first just be ATCG, then build from there.
        if get_hamming_distance(suffix_pattern, text) < mismatch:
            for nucleotide in {"A", "T", "C", "G"}:
                result.add(nucleotide + text) # From ATCG build AA AT AC AG and etc.
        else:
            result.add(pattern[0] + text) # If distance is bigger than the allowed mismatch
            # then add the current pattern + the suffix rebuilding the string as it is.
    return result
