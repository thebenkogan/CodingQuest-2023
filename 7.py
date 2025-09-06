from aoc import nums, read_input
from collections import deque

lines = read_input()

fruit = nums(lines[1])
fruits = []
for i in range(0, len(fruit), 2):
    fruits.append((fruit[i], fruit[i + 1]))

moves = [c for c in lines[3]]
move_map = {
    "D": (0, 1),
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
}

snake = deque([(0, 0)])
fi = 0
score = 0
for move in moves:
    hx, hy = snake[-1]
    dx, dy = move_map[move]
    nx, ny = hx + dx, hy + dy
    if nx < 0 or nx >= 20 or ny < 0 or ny >= 20:
        break

    if (nx, ny) == fruits[fi]:
        fi += 1
        score += 100
    else:
        snake.popleft()

    if (nx, ny) in snake:
        break
    snake.append((nx, ny))

    score += 1


print(score)
