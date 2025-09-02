from collections import defaultdict
from aoc import nums, read_input

lines = read_input()
results = defaultdict(int)
for line in lines:
    ns = nums(line)
    board = [["."] * 3 for _ in range(3)]
    player = "X"
    winner = None
    for n in ns:
        x, y = (n - 1) % 3, (n - 1) // 3
        board[y][x] = player

        for row in board:
            if all(c == player for c in row):
                winner = player

        for col in range(3):
            if all(row[col] == player for row in board):
                winner = player

        if all(c == player for c in [board[0][0], board[1][1], board[2][2]]):
            winner = player

        if all(c == player for c in [board[2][0], board[1][1], board[0][2]]):
            winner = player

        if winner:
            break
        player = "X" if player != "X" else "O"

    results["draw" if winner is None else winner] += 1

prod = 1
for v in results.values():
    prod *= v
print(prod)
