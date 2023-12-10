from hamming_distance import get_hamming_distance

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

print(neighbourhood("ACG"))

def neighbourhood_with_mismatch(pattern, mismatch):
    if mismatch == 0:
        return {pattern}
    if len(pattern) == 1:
        return {"A", "T", "C", "G"}
    result = set()
    suffix_pattern = pattern[1:]
    suffix_neighbours = neighbourhood_with_mismatch(suffix_pattern, mismatch)
    for text in suffix_neighbours:
        if get_hamming_distance(suffix_pattern, text) < mismatch:
            for nucleotide in {"A", "T", "C", "G"}:
                result.add(nucleotide + text)
        else:
            result.add(pattern[0] + text)
    return result
result = neighbourhood_with_mismatch("AGCAGGGTC", 2)
print(" ".join(result))



