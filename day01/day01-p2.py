import itertools
import numpy as np

with open("input.txt", "r") as f:
    entries = f.read().splitlines()

entries = [int(i) for i in entries]

for numbers in itertools.combinations(entries, 3):
    if sum(numbers) == 2020:
        print(np.prod(numbers))
        break

# If Python v3.8, can use math.prod instead
'''
Similar to p1, this is the three sum problem, which would combine
the original code I wrote for p1 with the dict, i.e. check the 
existence of the complement for each pair.
'''