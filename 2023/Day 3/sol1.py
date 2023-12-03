f = open("data.txt")
input_data = [list(line.strip()) for line in f]
sums = {}

for x, line in enumerate(input_data):
    for y, char in enumerate(line):
        if not char.isdigit() and char not in {".", "\n"}:
            for x1 in [-1, 0, 1]:
                for y1 in [-1, 0, 1]:
                    x2, y2 = x + x1, y + y1
                    if 0 <= x2 < len(input_data) and 0 <= y2 < len(line) and input_data[x2][y2].isdigit():
                        y3, y4 = y2, y2
                        while y3 >= 0 and input_data[x2][y3 - 1].isdigit():
                            y3 -= 1
                        while y4 < len(line) and input_data[x2][y4 + 1].isdigit():
                            y4 += 1
                        substring = "".join(input_data[x2][y3:y4 + 1])
                        sums[(x2, y3)] = int(substring)

total = sum(sums.values())
print(total)