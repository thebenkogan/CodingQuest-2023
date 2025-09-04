from aoc import read_input

lines = read_input()
parts = []
for line in lines:
    header = line[:4]
    if header != "5555":
        continue

    ship_number = int(line[4:12], 16)
    sequence_number = int(line[12:14], 16)
    checksum = int(line[14:16], 16)

    payload = line[16:64]
    b = bytearray(bytes.fromhex(payload))

    total = sum(b) % 256
    if total != checksum:
        continue

    parts.append((sequence_number, b.decode("ascii")))

print("".join(p for [_, p] in sorted(parts)))
