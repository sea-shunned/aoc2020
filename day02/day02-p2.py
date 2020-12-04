with open("input.txt", "r") as f:
    pwords = f.read().splitlines()

details = []

num_valid = 0

for line in pwords:
    # Split by space
    occ_range, letter, pword = line.split(" ")
    # Split occurence range
    occ_range = occ_range.split("-")
    # Convert to int
    min_occ, max_occ = int(occ_range[0]), int(occ_range[-1])
    # Remove the colon
    letter = letter[0]

    pos1 = pword[min_occ-1] == letter
    pos2 = pword[max_occ-1] == letter

    # Check if valid
    if pos1 != pos2:
        num_valid += 1

print(num_valid)