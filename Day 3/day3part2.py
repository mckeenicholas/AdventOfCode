
if __name__ == "__main__":
    f = open("data3.txt")
    count = 0
    lst = []
    for line in f:
        lst.append(line)
    for i in range(0, len(lst), 3):
        a = set(lst[i]).intersection(lst[i + 1]).intersection(lst[i + 2])
        if a.__contains__("\n"):
            a.remove("\n")
        num = ord(a.pop())-96
        if num < 0:
            num += 58
        count += num
    print(count)