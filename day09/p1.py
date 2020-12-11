with open("input.txt", "r") as f:
    input_numbers = f.read().splitlines()

input_numbers = [int(i) for i in input_numbers]

def two_sum(numbers, target):
    d = {}

    for num in numbers:
        complement = target-num
        if complement in d:
            if complement == num:
                continue
            else:
                return True, None
        d[num] = complement
    else:
        # print(sorted(numbers))
        # print(d)
        # print(target)
        return False, target

window_size = 25
lower = window_size
upper = lower + window_size

while upper < len(input_numbers):
    valid, num = two_sum(
        input_numbers[lower:upper],
        target=input_numbers[upper]
    )

    if not valid:
        print(input_numbers[upper])
        break
    else:
        lower += 1
        upper += 1