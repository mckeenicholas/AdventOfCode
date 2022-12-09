if __name__ == "__main__":
    f = open("data8.txt")
    trees = []
    for line in f:
        rows = []
        for char in line.strip():
            rows.append(int(char))
        trees.append(rows)
    scorelist = []
    for i, row in enumerate(trees):
        for j, tree in enumerate(row):
            distleft = 0
            for k in range(i - 1, -1, -1):
                distleft += 1
                if trees[k][j] >= trees[i][j]:
                    break
            distright = 0
            for k in range(i + 1, len(trees)):
                distright += 1
                if trees[k][j] >= trees[i][j]:
                    break
            distdown = 0
            for k in range(j - 1, -1, -1):
                distdown += 1
                if trees[i][k] >= trees[i][j]:
                    break
            distup = 0
            for k in range(j + 1, len(row)):
                distup += 1
                if trees[i][k] >= trees[i][j]:
                    break
            scorelist.append(distright * distleft * distdown * distup)
    print(max(scorelist))