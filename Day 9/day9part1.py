f = open("data9.txt")
positions = set()
headx = 0
heady = 0
tailx = 0
taily = 0
for line in f:
    for count in range(int(line[2:])):
        # Update head position
        if line[0] == "R":
            headx += 1
        elif line[0] == "L":
            headx -= 1
        elif line[0] == "U":
            heady += 1
        elif line[0] == "D":
            heady -= 1
        if abs(headx - tailx) > 1 or abs(heady - taily) > 1:
            # Update tail position
            # Check if head and tail are in the same row/column
            if headx == tailx or heady == taily:
                if headx - tailx > 1:
                    tailx += 1
                elif headx - tailx < -1:
                    tailx -= 1
                elif heady - taily > 1:
                    taily += 1
                elif heady - taily < -1:
                    taily -= 1
            else:
                # Move diagonally
                if headx > tailx and heady > taily:
                    tailx += 1
                    taily += 1
                elif headx > tailx and heady < taily:
                    tailx += 1
                    taily -= 1
                elif headx < tailx and heady > taily:
                    tailx -= 1
                    taily += 1
                elif headx < tailx and heady < taily:
                    tailx -= 1
                    taily -= 1
        print(f"{tailx}, {taily}")
        positions.add((tailx, taily))
print(len(positions))