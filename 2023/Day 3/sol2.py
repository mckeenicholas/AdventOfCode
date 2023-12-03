import math

f = open("data.txt")
input_data = [list(line) for line in f]
total = 0

for x, line in enumerate(input_data):
    for y, char in enumerate(line):
        if char == "*":
            ratio = {}
            for x1 in [-1, 0, 1]:
                for y1 in [-1, 0, 1]:
                    x2, y2 = x + x1, y + y1
                    if 0 <= x2 < len(input_data) and 0 <= y2 < len(line) and input_data[x2][y2].isdigit():
                        y3, y4 = y2, y2
                        while y3 >= 0 and input_data[x2][y3 - 1].isdigit():
                            y3 -= 1
                        while y4 < len(line) and input_data[x2][y4 + 1].isdigit():
                            y4 += 1
                        ratio[(x2, y3)] = int("".join(input_data[x2][y3:y4 + 1]))
            if len(ratio) == 2:
                total += math.prod(ratio.values())
print(total)