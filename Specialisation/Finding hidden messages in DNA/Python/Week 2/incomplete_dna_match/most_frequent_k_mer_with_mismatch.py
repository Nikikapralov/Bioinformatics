from hamming_distance import get_hamming_distance
from dna_neighbourhood import neighbourhood_with_mismatch

data = "TTGTGAGTTGTCATTGGGAGTCGTCGCATTGGCATTTGTTGGCATTTGTGAGTTGTTTGTTCGGAGTTGTCATGAGGAGTGGGAGTCGTGGCATCATTCGTGGTCGTGGTGGTCGTGGGAGCATTGGGAGTCGTTGTTCGTGGTGGTCGTGGTGGTGGGAGGAGGAGTTGTTCGCATCATGAGGAGCATTTGTTTGTTCGGAGTCGTCGTGGGAGCATTTGTTGGTGGTGGTCGCATGAGCATGAGGAGGAGTGGTTGTCATTCGTGGTGGCATCATCATTTGTTGGTCGCATGAGTCGTGGTTGTTCGTCGTGGGAGTGGGAGGAGTCG"
k_mer_length = 6
mismatch = 3

"""
This algorithm finds the most frequent k_mer with a mismatch that already exists in a DNA strand.
For example if we have AAAGCTGAA
The most frequent will be AAA:
[('AAA', 3), ('AAG', 2), ('GAA', 2), ('AGC', 1), ('GCT', 1), ('CTG', 1), ('TGA', 1)]
Although a good algorithm, it unfortunately does not answer the question provided by the task itself.
I now understand that we must also see and account for each possible mutation.
This would require a new algorithm.
"""
def most_frequent_k_mer_with_mismatch_no_mutations(data, k_mer_length, mismatch):
    maximum_point = len(data) - k_mer_length + 1
    all_k_mers_from_text = {}
    for i in range(maximum_point):
        k_mer = data[i:i+k_mer_length]
        if k_mer in all_k_mers_from_text:
            all_k_mers_from_text[k_mer] += 1
        else:
            all_k_mers_from_text[k_mer] = 1

    print(all_k_mers_from_text)

    for k_mer_one in all_k_mers_from_text:
        for k_mer_two in all_k_mers_from_text:
            if k_mer_one == k_mer_two:
                continue
            if get_hamming_distance(k_mer_one, k_mer_two) <= mismatch:
                all_k_mers_from_text[k_mer_one] += 1

    sorted_k_mers = sorted(all_k_mers_from_text.items(), key=lambda x: x[1], reverse=True)
    highest_number_count = sorted_k_mers[0][1]
    most_frequent_k_mers_with_mismatch = []

    for k_mer, count in sorted_k_mers:
        if count == highest_number_count:
            most_frequent_k_mers_with_mismatch.append(k_mer)
        else:
            break

    print(all_k_mers_from_text)
    print(sorted_k_mers)
    print(most_frequent_k_mers_with_mismatch)
    return most_frequent_k_mers_with_mismatch





# result = inefficient_most_frequent_k_mer_with_mismatch(data, k_mer_length, mismatch)
# print(" ".join(result))

"""
This algorithm takes into account all possible mutations as well.
"""
def most_frequent_k_mers_with_mismatch_mutations_too(data, k_mer_length, mismatch):
    frequency_map = {}
    data_length = len(data)
    for i in range(data_length - k_mer_length):
        pattern = data[i:i + k_mer_length]
        neighbourhood = neighbourhood_with_mismatch(pattern, mismatch)
        for neighbour in neighbourhood:
            if neighbour not in frequency_map:
                frequency_map[neighbour] = 1
            else:
                frequency_map[neighbour] += 1

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

