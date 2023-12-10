"""
The skew is the difference between the total amount of C and the total amount of G.
Why is it important? Well, we learned that due to the existence of Okazaki Fragments and the way
they are created, we may have a potentially higher deamination count on the lagging strand as compared
to the leading strand. This results in C deaminating to T and lowering the C content on the lagging strand,
as compared to the one on the leading strand which remains relatively intact. (Remember that the bacterial
chromosome is replicated from 2 directions, which results in one chromosome copy having one half a lagging and
one half a leading strand).
"""
import os

from utils.utils import get_data
path = os.path.join(os.curdir, "dataset.txt")
data = get_data(path)
print(*data)

bases_skew_dictionary = {
    "A": 0,
    "T": 0,
    "G": 1,
    "C": -1,
}

def get_skew(data: str):
    skew_list = ["0"]
    current_skew = 0
    for base in data:
        current_skew += bases_skew_dictionary[base]
        skew_list.append(str(current_skew))
    return skew_list

print(" ".join(get_skew(data)))