with open("input.txt", "r") as f:
    answers = f.read().split("\n\n")

num_answered = 0

for group in answers:
    group = group.replace("\n", "")
    num_answered += len(set(group))

print(num_answered)