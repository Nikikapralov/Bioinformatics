import os
import matplotlib.pyplot as plt
from utils.utils import get_data
from Week_2.skew.skew import get_skew
from Week_2.skew.skew_minimum import get_minimum_skew_from_diagram
from Week_2.incomplete_dna_match.most_frequence_k_mer_with_mismatch_and_reverse_complement import most_frequent_k_mer_with_mismatch_and_reverse_complement

path = os.path.join(os.curdir, "Salmonella_enterica.txt")
k_mer_length = 9
mismatch = 1
data = get_data(path) # Extract the data.
skew_data = [int(el) for el in get_skew(data)]
data_index = [i for i, val in enumerate(data)]
# Find and plot the skew.
skew_diagram = plt.plot(data_index, skew_data)
plt.show()
# Find the skew minimum position. This is where the OriC should be.
skew_minimum = get_minimum_skew_from_diagram(skew_data)
position_of_oriC = int(skew_minimum[0][0])
# After we know the skew minimum, we can now check for 9-mers (reverses also) in a range
# 500 bases where the skew is in the middle, the start and the end.
base_range = 500
middle = data[int(position_of_oriC-base_range/2) : int(position_of_oriC+base_range/2)]
start = data[position_of_oriC:position_of_oriC + base_range]
end = data[position_of_oriC-base_range:position_of_oriC]
print(position_of_oriC)

middle_result = most_frequent_k_mer_with_mismatch_and_reverse_complement(middle, k_mer_length, mismatch)
print(f"Middle: {middle_result}")
start_result = most_frequent_k_mer_with_mismatch_and_reverse_complement(start, k_mer_length, mismatch)
print(f"Start: {start_result}")
end_result = most_frequent_k_mer_with_mismatch_and_reverse_complement(end, k_mer_length, mismatch)
print(f"End: {end_result}")

data = "aatgatgatgacgtcaaaaggatccggataaaacatggtgattgcctcgcataacgcggtatgaaaatggattgaagcccgggccgtggattctactcaactttgtcggcttgagaaagacctgggatcctgggtattaaaaagaagatctatttatttagagatctgttctattgtgatctcttattaggatcgcactgcccTGTGGATAAcaaggatccggcttttaagatcaacaacctggaaaggatcattaactgtgaatgatcggtgatcctggaccgtataagctgggatcagaatgaggggTTATACACAactcaaaaactgaacaacagttgttcTTTGGATAActaccggttgatccaagcttcctgacagagTTATCCACAgtagatcgcacgatctgtatacttatttgagtaaattaacccacgatcccagccattcttctgccggatcttccggaatgtcgtgatcaagaatgttgatcttcagtg"
data = data.upper()

result = most_frequent_k_mer_with_mismatch_and_reverse_complement(data, 9, 1)
result_in_string = [entry for entry in result if entry in data]
print(result)
print(result_in_string)

