f = open("data10.txt")
value = 1
column = 0
pixel_line = ""
for line in f:
    if line.strip() == "noop":
        if column % 40 in [value - 1, value, value + 1]:
            pixel_line += "#"
        else:
            pixel_line += "."
        column += 1
    else:
        num = int(line.strip()[4:])
        if column % 40 in [value - 1, value, value + 1]:
            pixel_line += "#"
        else:
            pixel_line += "."
        column += 1
        if column % 40 in [value - 1, value, value + 1]:
            pixel_line += "#"
        else:
            pixel_line += "."
        column += 1
        value += num
for i in range(0, len(pixel_line), 40):
    print(pixel_line[i:i+39])
