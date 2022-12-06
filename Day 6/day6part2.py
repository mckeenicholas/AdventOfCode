
if __name__ == "__main__":
    f = open("data6.txt")
    line = f.readline()
    for i in range(len(line)-14):
        subline = line[i:i+14]
        chars = []
        for char in subline:
            if char in chars:
                break
            else:
                chars.append(char)
            if len(chars) == 14:
                print(i+14)
                quit()