"""
The difference between the 2 strings is called the hamming distance. For example AAA and AAB are different in 1 letter,
hamming distance of 1.
"""

def get_hamming_distance(data, match):
    hamming_distance = 0
    for index, base in enumerate(match):
        if base != data[index]:
            hamming_distance += 1
    return hamming_distance
