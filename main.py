
if __name__ == "__main__":
    f = open("data.txt")
    line = f.readline()
    data = []
    while line != "":
        data.append(line)
        line = f.readline()
    totals = [0]
    elf = 0
    for item in data:
        if item == "\n":
            elf += 1
            totals.append(0)
        else:
            totals[elf] += int(item)
    print(max(totals))
    max1 = max(totals)
    totals.remove(max1)
    max2 = max(totals)
    totals.remove(max2)
    max3 = max(totals)
    print(max1 + max2 + max3)
