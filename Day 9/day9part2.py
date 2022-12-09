
def follow(head: list, tail: list):
    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
        # Update tail position
        # Check if head and tail are in the same row/column
        if head[0] == tail[0] or head[1] == tail[1]:
            if head[0] - tail[0] > 1:
                tail[0] += 1
            elif head[0] - tail[0] < -1:
                tail[0] -= 1
            elif head[1] - tail[1] > 1:
                tail[1] += 1
            elif head[1] - tail[1] < -1:
                tail[1] -= 1
        else:
            # Move diagonally
            if head[0] > tail[0] and head[1] > tail[1]:
                tail[0] += 1
                tail[1] += 1
            elif head[0] > tail[0] and head[1] < tail[1]:
                tail[0] += 1
                tail[1] -= 1
            elif head[0] < tail[0] and head[1] > tail[1]:
                tail[0] -= 1
                tail[1] += 1
            elif head[0] < tail[0] and head[1] < tail[1]:
                tail[0] -= 1
                tail[1] -= 1


f = open("data9.txt")
positions = set()
snake = [[0, 0] for i in range(10)]

for line in f:
    for count in range(int(line[2:])):
        # Update head position
        if line[0] == "R":
            snake[0][0] += 1
        elif line[0] == "L":
            snake[0][0] -= 1
        elif line[0] == "U":
            snake[0][1] += 1
        elif line[0] == "D":
            snake[0][1] -= 1
        for i in range(len(snake) - 1):
            follow(snake[i], snake[i + 1])
        positions.add((snake[9][0], snake[9][1]))
print(len(positions))