def find_hidden_message_count(text, template):
    start = 0
    end = len(template)
    count = 0
    while True:
        if end > len(text) - 1:
            break
        if text[start:end] == template:
            count += 1
        start += 1
        end += 1
    return count

text = "GACCATCAAAACTGATAAACTACTTAAAAATCAGT"
template = "AAA"

result = find_hidden_message_count(text, template)
print(result)