
if __name__ == "__main__":
    f = open("data4.txt")
    count = 0
    for l in f:
        jobs = []
        line = l.strip()
        p1 = line[:line.find(",")]
        p2 = line[line.find(",") + 1:]
        f1 = int(p1[:p1.find("-")])
        f2 = int(p1[p1.find("-") + 1:])
        s1 = int(p2[:p2.find("-")])
        s2 = int(p2[p2.find("-") + 1:])
        if (s1 <= f1 <= s2) or (f1 <= s1 <= f2) or (s1 <= f2 <= s2) or (f1 <= s2 <= f2):
            count += 1
    print(count)
