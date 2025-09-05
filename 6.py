from aoc import nums, read_input
from dataclasses import dataclass
from typing import Tuple


@dataclass
class Asteroid:
    x: float
    y: float
    vx: float
    vy: float

    def pos_after_duration(self, t: float) -> Tuple[float, float]:
        return self.x + (self.vx * t), self.y + (self.vy * t)


asteroids = []
for line in read_input():
    x, y, vx, vy = nums(line)
    asteroids.append(Asteroid(x, y, vx, vy))

timeToPositions = {}
for t in range(3601, 3660):
    positions = set()
    for asteroid in asteroids:
        x, y = asteroid.pos_after_duration(t)
        if 0 <= x <= 99 and 0 <= y <= 99:
            positions.add((x, y))
    timeToPositions[t] = positions

for x in range(0, 100):
    for y in range(0, 100):
        if all((x, y) not in timeToPositions[t] for t in range(3601, 3660)):
            print(f"{x}:{y}")
            exit()
