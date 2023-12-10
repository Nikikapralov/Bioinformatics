def get_data(path):
    with open(path, "r") as file:
        data = "".join([line.strip() for line in file.readlines()])
    return data


def get_max_count(data):
    sorted_k_mers = sorted(data.items(), key=lambda x: x[1], reverse=True)
    highest_number_count = sorted_k_mers[0][1]
    most_frequent_k_mers_with_mismatch = []

    for k_mer, count in sorted_k_mers:
        if count == highest_number_count:
            most_frequent_k_mers_with_mismatch.append(k_mer)
        else:
            break
    return most_frequent_k_mers_with_mismatch