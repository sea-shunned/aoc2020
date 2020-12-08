with open("input.txt", "r") as f:
    pport_data = f.read().split("\n\n")

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

num_valid = 0

for pport in pport_data:
    pport = pport.replace("\n", " ").split(" ")

    if len(pport) < len(required_fields):
        continue
    elif len(pport) == len(required_fields):
        for field in pport:
            if "cid" in field:
                break
        else:
            num_valid += 1
    else:
        num_valid += 1

print(num_valid)