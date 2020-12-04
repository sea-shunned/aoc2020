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
    counter = 0
    # Check password
    # No need to for collections here
    for l in pword:
        if l == letter:
            counter += 1
    # Check if valid
    if counter >= min_occ and counter <= max_occ:
        num_valid += 1

print(num_valid)