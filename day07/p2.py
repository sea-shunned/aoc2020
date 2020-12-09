import re
# Let's try a graph solution for this one
import networkx as nx

with open("input.txt", "r") as f:
    rules = f.read().splitlines()

rule_dict = {}
target = "shiny gold"

contents_regex = re.compile("([0-9]) (\w+ \w+)")

g = nx.DiGraph()

for rule in rules:
    colour, contents = rule.split(" bags contain ")
    g.add_node(colour)
    if contents[:2] != "no":
        for number, content_colour in contents_regex.findall(rule):
            g.add_edge(colour, content_colour, number=int(number))


def traverse_graph(g, target):
    if len(g[target]) == 0:
        return 0
    else:
        return sum([
            traverse_graph(g, node) * w["number"] + w["number"] for node, w in g[target].items()
        ])


print(traverse_graph(g, target))
