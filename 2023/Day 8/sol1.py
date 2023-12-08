with open("data.txt") as file:
    sequence = file.readline().strip()
    moves = {line[:3]: (line[7:10], line[12:15]) for line in file.readlines()[1:]}

pos, count = "AAA", 0

while pos != "ZZZ":
    move = sequence[count % len(sequence)]
    count += 1
    pos = moves[pos][move == "R"]

print(count)
