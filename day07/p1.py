import re

with open("input.txt", "r") as f:
    rules = f.read().splitlines()

rule_dict = {}
target = "shiny gold"

contents_regex = re.compile("([0-9]) (\w+ \w+)")

for rule in rules:
    colour, contents = rule.split(" bags contain ")
    rule_dict[colour] = {}
    if contents[:2] != "no":
        for number, content_colour in contents_regex.findall(rule):
            rule_dict[colour][content_colour] = int(number)

def check_target(colour):
    bag_colours = rule_dict[colour].keys()
    return target in bag_colours or any((check_target(colour) for colour in bag_colours))

print(sum(check_target(colour) for colour in rule_dict.keys()))