#get data from file (file must be in same directory as other .py files!
with open('dataset_2_13.txt') as file:
    for index, line in enumerate(file):
        if index == 0:
            data = line
        elif index == 1:
            template_length = int(line)

dict_of_substrings = {}

data = "CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA"
template_length = 3

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


def get_substring_with_highest_count(dict_of_substrings):
    result = []
    ordered = sorted(dict_of_substrings.items(), key=lambda x: x[1], reverse=True)
    highest = ordered[0][1]
    for template, frequency in ordered:
        if frequency < highest:
            return " ".join(result)
        result.append(template)


dictionary = find_all_substrings_and_counts(data, template_length)
result = get_substring_with_highest_count(dictionary)
print(result)
