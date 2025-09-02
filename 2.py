from collections import Counter
from aoc import read_input

lines = read_input()
count = 0
total = 0
for line in lines:
    n = int(line)
    c = Counter(bin(n)[2:])
    if c["1"] % 2 == 1:
        continue
    count += 1
    total += n & 0b0111_1111_1111_1111

print(round(total / count))
