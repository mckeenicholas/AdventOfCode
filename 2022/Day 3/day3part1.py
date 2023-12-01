
if __name__ == "__main__":
    f = open("data3.txt")
    count = 0
    for line in f:
        a = set(line[:len(line) // 2]).intersection(line[len(line) // 2:])
        num = ord(a.pop())-96
        if num < 0:
            num += 58
        count += num
    print(count)