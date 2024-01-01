import math
entropy = 0
values = [0.25, 0.0, 0.25, 0.5]
for value_for_entropy in values:
    if value_for_entropy == 0:
        continue
    entropy += -(value_for_entropy * math.log(value_for_entropy, 2))
print(entropy)

# A - 1 B - 2 C - 0.0 D 1.5