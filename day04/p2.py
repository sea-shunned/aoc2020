import re

with open("input.txt", "r") as f:
    pport_data = f.read().split("\n\n")

validity_checker = {
    "byr": re.compile("byr:(19[2-9][0-9]|200[0-2])"),
    "iyr": re.compile("iyr:(201[0-9]|2020)"),
    "eyr": re.compile("eyr:(202[0-9]|2030)"),
    "hgt": re.compile("hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)"),
    "hcl": re.compile("hcl:#([0-9a-f]{6})"),
    "ecl": re.compile("ecl:(amb|blu|brn|gry|grn|hzl|oth)"),
    "pid": re.compile("pid:[0-9]{9}(\s|$)")
}

num_valid = 0

for pport in pport_data:
    pport = pport.replace("\n", " ")
    # print(pport)
    for regex_expr in validity_checker.values():
        # print(len(regex_expr.findall(pport)))
        # print(regex_expr)
        if not regex_expr.search(pport):
            # print(regex_expr, pport)
            break
    else:
        print(pport)
        num_valid += 1

print(num_valid)

'''
A single regex string, with each sub string, requiring 7 matches would be
another approach so you don't have to search each expression through the
whole string.
'''