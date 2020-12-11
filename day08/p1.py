with open("input.txt", "r") as f:
    ops = f.read().splitlines()

lines_encountered = set()

current_line = 0
accumulator = 0

while True:
    line = ops[current_line]

    op, val = line.split(" ")
    val = int(val)

    if op == "acc":
        accumulator += val
        current_line += 1
    elif op == "jmp":
        current_line += val
    elif op == "nop":
        current_line += 1
    if current_line in lines_encountered:
        break
    else:
        lines_encountered.add(current_line)

print(lines_encountered)
print(accumulator)