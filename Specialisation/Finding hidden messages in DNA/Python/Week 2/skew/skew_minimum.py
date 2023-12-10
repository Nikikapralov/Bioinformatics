import os
import sys

from utils.utils import get_data
path = os.path.join(os.curdir, "dataset.txt")
data = get_data(path)

bases_skew_dictionary = {
    "A": 0,
    "T": 0,
    "G": 1,
    "C": -1,
}

"""
Find the position in the skew diagram where it attains a minimum. So first we need to generate the skew diagram
and then need to find its minimum. It is possible that there are multiple minimums with the same value so we need
to provide all of them. Would this imply two OriC genomes?
Here I have implemented 2 loops since I was having trouble understanding the task. It can actually be done with one
loop, but I will not implement it here since it is trivial.
"""


def get_skew_diagram(data):
    current_skew = 0
    skew_results = [(current_skew, 0)]
    for index, base in enumerate(data):
        if base == "\n":
            continue
        current_skew += bases_skew_dictionary[base]
        skew_results.append((current_skew, index + 1))
    return skew_results


def get_minimum_skew_from_diagram(skew_results):
    current_minimum_skew_list = []
    current_minimum = sys.maxsize

    for skew, index in skew_results:
        if skew < current_minimum:
            current_minimum = skew
            current_minimum_skew_list = [str(index)]

        elif skew == current_minimum:
            current_minimum_skew_list.append(str(index))

    return current_minimum_skew_list



skew_list = get_skew_diagram(data)
skew_minimum_list = get_minimum_skew_from_diagram(skew_list)
print(" ".join(skew_minimum_list))