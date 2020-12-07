with open("input.txt", "r") as f:
    geology = f.read().splitlines()

pos = (0, 0)
# 3 right, 1 down
movement = (3, 1)
width = len(geology[0])
num_trees = 0

while pos[1] < len(geology) - 1:
    pos = ((pos[0] + movement[0]) % width, pos[1] + movement[1])
    col, row = pos[0], pos[1]

    if geology[row][col] == "#":
        num_trees += 1

print(num_trees)