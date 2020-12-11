with open("input.txt", "r") as f:
    input_numbers = f.read().splitlines()

input_numbers = [int(i) for i in input_numbers]

# From part 1
target = 257342611

total = 0
new_total = 0
sequence = []

for num in input_numbers:
    if total < target:
        sequence.append(num)
        total += num
    if total == target:
        print(min(sequence) + max(sequence))
        break
    while total > target:
        total -= sequence[0]
        sequence = sequence[1:]
