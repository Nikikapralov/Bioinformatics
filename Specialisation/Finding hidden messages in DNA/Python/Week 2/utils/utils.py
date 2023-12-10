def get_data(path):
    with open(path, "r") as file:
        data = "".join(file.readlines())
    return data