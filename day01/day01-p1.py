import itertools

with open("input.txt", "r") as f:
    entries = f.read().splitlines()

entries = [int(i) for i in entries]

for num1, num2 in itertools.combinations(entries, 2):
    if (num1 + num2) == 2020:
        print(num1*num2)
        break

'''
For future reference, this is the classic two-sum problem, where
the efficient solution is to use a dict to store the complement
for each number, and check if complement exists in the dict.
'''
