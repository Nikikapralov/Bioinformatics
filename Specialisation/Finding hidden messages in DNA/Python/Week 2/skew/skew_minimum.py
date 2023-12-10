
import sys


"""
Find the position in the skew diagram where it attains a minimum. So first we need to generate the skew diagram
and then need to find its minimum. It is possible that there are multiple minimums with the same value so we need
to provide all of them. Would this imply two OriC genomes?
Here I have implemented 2 loops since I was having trouble understanding the task. It can actually be done with one
loop, but I will not implement it here since it is trivial.
"""


def get_minimum_skew_from_diagram(skew_results):
    current_minimum_skew_list = []
    current_minimum = sys.maxsize

    for index, skew in enumerate(skew_results):
        if skew < current_minimum:
            current_minimum = skew
            current_minimum_skew_list = [(str(index), str(skew))]

        elif skew == current_minimum:
            current_minimum_skew_list.append((str(index), str(skew)))

    return current_minimum_skew_list

print(get_minimum_skew_from_diagram([int(x) for x in ['0', '0', '0', '0', '-1', '-1', '-2', '-2', '-2', '-3', '-4', '-5', '-4', '-4', '-3', '-3', '-3', '-2', '-1', '-1', '-1', '-2', '-2', '-1']]))