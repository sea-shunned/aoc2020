import numpy as np

with open("input.txt", "r") as f:
    geology = f.read().splitlines()

movements = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_list = []

for movement in movements:
    pos = (0, 0)
    width = len(geology[0])
    num_trees = 0

    while pos[1] < len(geology) - 1:
        pos = ((pos[0] + movement[0]) % width, pos[1] + movement[1])
        col, row = pos[0], pos[1]

        if geology[row][col] == "#":
            num_trees += 1
    tree_list.append(num_trees)

print(np.prod(tree_list))