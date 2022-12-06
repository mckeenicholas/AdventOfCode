
if __name__ == "__main__":
    f = open("data6.txt")
    line = f.readline()
    for i in range(len(line)-4):
        subline = line[i:i+4]
        chars = []
        for char in subline:
            if char in chars:
                break
            else:
                chars.append(char)
            if len(chars) == 4:
                print(i+4)
                quit()