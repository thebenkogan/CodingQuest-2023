from collections import defaultdict
from aoc import read_input

lines = read_input()
totals = defaultdict(int)
for line in lines:
    split = line.split(" ")
    category = split[2]
    quantity = int(split[1])
    totals[category] += quantity

prod = 1
for v in totals.values():
    prod *= v % 100

print(prod)
