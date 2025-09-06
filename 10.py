import heapq
import re
from aoc import read_input


lines = read_input()
adj = {}
for line in lines:
    ns = [(n, int(c) + 600) for n, c in re.findall(r"([A-Z]{3}):(\d+)", line)]
    start = line.split(" ")[0]
    adj[start] = ns


start = "TYC"
end = "EAR"

seen = set()
q = [(0, start)]
while len(q) > 0:
    c, n = heapq.heappop(q)
    if n == end:
        print(c)
        exit()

    if n in seen:
        continue
    seen.add(n)

    for neighbor, cost in adj[n]:
        if neighbor == end:
            cost -= 600
        if neighbor not in seen:
            heapq.heappush(q, (c + cost, neighbor))
