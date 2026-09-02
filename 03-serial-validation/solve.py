import itertools
import string

target = 360

chars = string.ascii_uppercase + string.digits

for combination in itertools.product(chars, repeat=6):
    candidate = "".join(combination)

    total = sum(ord(c) for c in candidate)

    if total == target:
        print("REV-" + candidate)
        break
