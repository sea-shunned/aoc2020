with open("input.txt", "r") as f:
    ops = f.read().splitlines()


def acc(index, value, accumulator):
    return index + 1, accumulator + value

def jmp(index, value):
    return index + value

def nop(index):
    return index + 1

def execute(ops, accumulator=0):
    current_line = 0
    lines_encountered = set()

    while True:
        line = ops[current_line]

        op, val = line.split(" ")
        val = int(val)
        if op == "acc":
            current_line, accumulator = acc(current_line, val, accumulator)
        elif op == "jmp":
            current_line = jmp(current_line, val)
        elif op == "nop":
            current_line = nop(current_line)
        if current_line in lines_encountered:
            return False, accumulator
        elif current_line == len(ops):
            return True, accumulator
        else:
            lines_encountered.add(current_line)


i = 0
while True:
    modified_ops = ops.copy()
    for line_num, line in enumerate(ops[i:]):
        op, val = line.split(" ")
        if op == "nop":
            modified_ops[i+line_num] = f"jmp {val}"
            break
        elif op == "jmp":
            modified_ops[i+line_num] = f"nop {val}"
            break
    valid, accumulator = execute(modified_ops)
    if valid:
        print(accumulator)
        break
    else:
        i += 1

'''
To minimize time, I gave up and brute-forced. I thought by reversing
through the instructions, the first line we encounter that exists in
our infinite loop will be the one that needs to change, but I wasn't
able to get it to work for the full input (worked for example).

See https://old.reddit.com/r/adventofcode/comments/k8zdx3/day_8_part_2_without_bruteforce/gf1e5m4/ for some details and Rust
example for this kind of approach. Peter Norvig used brute-force,
so I'm in good company!
'''