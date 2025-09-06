from itertools import permutations
from aoc import nums, read_input

lines = read_input()
adj = [nums(row) for row in lines]

nodes = [i for i in range(1, len(adj))]
ps = permutations(nodes)

best = 1e10
for p in ps:
    cost = adj[0][p[0]] + adj[p[-1]][0]
    for i in range(len(p) - 1):
        cost += adj[p[i]][p[i + 1]]
    best = min(best, cost)

print(best)
