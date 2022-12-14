class Caves:
    def __init__(self, cave):
        self.cave = cave

    def place(self, x, y):
        if y < len(cave[0]) - 1:
            if cave[x][y + 1] == ".":
                return self.place(x, y + 1)
            elif cave[x - 1][y + 1] == ".":
                return self.place(x - 1, y + 1)
            elif cave[x + 1][y + 1] == ".":
                return self.place(x + 1, y + 1)
            else:
                if self.cave[x][y] == "o":
                    return False
                else:
                    self.cave[x][y] = "o"
                    return True
        else:
            return False

    def __str__(self):
        lines = ""
        for i in range(len(cave[0])):
            line = ""
            for j in range(len(cave)):
                line += cave[j][i]
            lines += line + "\n"
        return lines


f = open("data14.txt")
lines = [n.strip().split(" -> ") for n in f]
cave = [["." for i in range(175)] for j in range(700)]
for line in lines:
    direction = []
    for dir in line:
        direction.append((int(dir.split(",")[0]), int(dir.split(",")[1])))
    for i in range(len(direction) - 1):
        for j in range(direction[i][0], direction[i + 1][0] + 1):
            cave[j][direction[i][1]] = "#"
        for j in range(direction[i][1], direction[i + 1][1] + 1):
            cave[direction[i][0]][j] = "#"
        for j in range(direction[i + 1][0], direction[i][0] + 1):
            cave[j][direction[i][1]] = "#"
        for j in range(direction[i + 1][1], direction[i][1] + 1):
            cave[direction[i][0]][j] = "#"

for line in cave:
    line[169] = "#"

# Sand stuff
full = False
c = Caves(cave)

while not full:
    if not c.place(500, 0):
        full = True

print(c)
print(c.__str__().count("o"))