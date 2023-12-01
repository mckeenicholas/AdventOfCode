
if __name__ == "__main__":
    crates = [[] for _ in range(9)]
    lines = []
    f = open("crates.txt")
    for line in f:
        lines.append(line)
    for i in range(7, -1, -1):
        for j in range(9):
            if lines[i][1:2] != " ":
                crates[j].append(lines[i][1:2])
            lines[i] = lines[i][4:]

    f2 = open("moves.txt")
    for line in f2:
        num = int(line[5:7])
        movefrom = int(line[line.find("from")+5:line.find("to")])
        moveto = int(line.strip()[line.find("to")+3:])
        for _ in range(num):
            crates[moveto-1].append(crates[movefrom-1].pop())
    ans = ""
    for stack in crates:
        ans += stack.pop()
    print(ans)
