import math

with open("data.txt") as file:
    sequence = file.readline().strip()
    moves = {line[:3]: (line[7:10], line[12:15]) for line in file.readlines()[1:]}

nodes = [m for m in moves.keys() if m.endswith("A")]
cycles = []

for node in nodes:
    count = 0
    while not node.endswith("Z"):
        move = sequence[count % len(sequence)]
        node = moves[node][move == "R"]
        count += 1
    cycles.append(count)

print(math.lcm(*cycles))
