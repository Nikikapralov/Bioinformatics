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
times = 3


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

#After optimisation, it now needs around 4 seconds! Much better :). This does require a more algorithmic approach though,
#and may pose a significant challenge to unseasoned practicioners. Can it get faster? For sure! But I'd rather deal with the
#other materials of the course, and besides, there are enough free tools on the internet, who do the same job :)
#Hint: Try writing it in Cython, C++ or even C! If you opt for a better algorithmic approach and confer to numba rules, you may
#even get it to milliseconds range! But is the roughly 3 seconds speedup worth the time investment?