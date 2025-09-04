from aoc import nums, read_input

WIDTH = 50
HEIGHT = 10

lines = read_input()
grid = [["."] * WIDTH for _ in range(HEIGHT)]
for line in lines:
    sx, sy, w, h = nums(line)
    for x in range(sx, sx + w):
        for y in range(sy, sy + h):
            grid[y][x] = "." if grid[y][x] == "#" else "#"

for row in grid:
    print("".join(row))
