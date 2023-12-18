genome = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
with open("E_coli.txt") as file:
    for line in file:
        if line.startswith("A") or line.startswith("T") or line.startswith("G") or line.startswith("C"):
            genome += line
        else:
            k, length, times = line.split()
            k = int(k)
            length = int(length)
            times = int(times)
k = 9
length = 500
times = 9


def build_k_mer_frequency_dict(genome):
    k_mers = {}
    for i in range(len(genome) - k):
        current_k_mer = genome[i:i+k]
        if current_k_mer not in k_mers:
            k_mers[current_k_mer] = [i]
        else:
            k_mers[current_k_mer].append(i)
    return k_mers


def calculate_amount_of_clumps(k, length, times, k_mers_dict):
    result = []
    for key, value in k_mers_dict.items():
        if len(value) >= times:
            for index in range(len(value) - times + 1):
                total = length - k
                potential_clump = value[index:index+times]
                start = potential_clump[0]
                end = potential_clump[-1]
                if end - start <= total:
                    result.append(key)
                    break

    return result







k_mers_dict = build_k_mer_frequency_dict(genome)
result = calculate_amount_of_clumps(k=k, k_mers_dict=k_mers_dict, length=length, times=times)
print(result)
print(len(result))

"""
What usually happens is we go for the brute force approach. We try to loop way too many times, which ultimately is
useless. Instead, what we want to do is just 2 loops. First loop to build all the k_mers and insert them in a dict.
And second loop to add a +1 to each encountered k-mer.
What we otherwise end up doing is pretty much this: From 1 to 500 loop and find K-mers. Then from 2 to 501 loop and find
k-mers and so on and so forth. This is useless. Just loop once to build the map. Loop second time to fill it.
"""

#After optimisation, it now needs around 4 seconds! Much better :). This does require a more algorithmic approach though,
#and may pose a significant challenge to unseasoned practicioners. Can it get faster? For sure! But I'd rather deal with the
#other materials of the course, and besides, there are enough free tools on the internet, who do the same job :)
#Hint: Try writing it in Cython, C++ or even C! If you opt for a better algorithmic approach and confer to numba rules, you may
#even get it to milliseconds range! But is the roughly 3 seconds speedup worth the time investment?