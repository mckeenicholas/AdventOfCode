from collections import deque

if __name__ == "__main__":
    f = open("data12")
    lines = f.read().split()
    map = [list(line) for line in lines]
    x = 0
    y = 0
    for a, line in enumerate(lines):
        if "E" in line:
            x = a
            y = line.index("E")
    end = (x, y)
    map[x][y] = "{"
    for a, line in enumerate(lines):
        if "S" in line:
            x = a
            y = line.index("S")
    map[x][y] = "a"
    start = (x, y)

    loc = {}
    # Create a dictionary for each location, containing the squares it can go to
    for x in range(len(map)):
        for y in range(len(map[0])):
            loc[(x, y)] = []
            if x > 0 and ord(map[x][y]) >= ord(map[x - 1][y]) - 1:
                loc[(x, y)].append((x - 1, y))
            if x < len(map) - 1 and ord(map[x][y]) >= ord(map[x + 1][y]) - 1:
                loc[(x, y)].append((x + 1, y))
            if y > 0 and ord(map[x][y]) >= ord(map[x][y - 1]) - 1:
                loc[(x, y)].append((x, y - 1))
            if y < len(map[0]) - 1 and ord(map[x][y]) >= ord(map[x][y + 1]) - 1:
                loc[(x, y)].append((x, y + 1))

    d = []
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == "a":
                # BFS algorithm
                start = (x, y)
                queue = deque([start])
                distances = {start: 0}
                found = False
                while queue:
                    location = queue.popleft()
                    if end in queue:
                        found = True
                        break
                    else:
                        for adj in loc[location]:
                            if adj not in distances.keys() or distances[location] + 1 < distances[adj]:
                                queue.append(adj)
                                distances[adj] = distances[location] + 1
                if found:
                    d.append(distances[end])
    print(min(d))