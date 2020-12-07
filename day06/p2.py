import string

with open("input.txt", "r") as f:
    answers = f.read().split("\n\n")

num_answered = 0

for group in answers:
    base = set(string.ascii_lowercase)

    for answer in group.split("\n"):
        if not answer:
            continue
        base = base.intersection(set(answer))
    num_answered += len(base)

print(num_answered)