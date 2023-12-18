import numba

@numba.njit(cache=True)
def find_all_substrings_and_counts(data, template_length):
    dict_of_substrings = {}
    start = 0
    end = template_length
    while True:
        if end > len(data) - 1:
            return dict_of_substrings
        current_substring = data[start:end]
        if current_substring in dict_of_substrings:
            dict_of_substrings[current_substring] += 1
        else:
            dict_of_substrings[current_substring] = 1
        start += 1
        end += 1

genome = ""
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

@numba.njit(cache=True)
def get_results(genome, length, k):
    results = []
    for i in range(len(genome) - length):
        data = genome[i:i+length]
        dictionary = find_all_substrings_and_counts(data, k)
        for key, value in dictionary.items():
            if value >= times:
                results.append(key)
    return results

results = get_results(genome, length, k)
print(len(set(results)))

#Naive implementation. Around 99% of the loops are unneeded and just a waste of time. It takes a couple of hours to finishe,
#I guess, I never waited for it. Instead, I applied some numba optimisation. Now it takes around 4-5 minutes. Not exceptional,
#but considering it took me around 5 minutes to write the code and optimise it, not bad either :) Good enough if your internet is
#down and you need to do some calculations, but don't have the time/knowledge to code the more efficient version.