
if __name__ == "__main__":
    f = open("data8.txt")
    trees = []
    treecount = []
    for line in f:
        rows = []
        countRows = []
        for char in line.strip():
            rows.append(int(char))
            countRows.append(0)
        trees.append(rows)
        treecount.append(countRows)
    for i in range(0, len(trees[0])):
        height = -1
        height2 = -1
        for j in range(0, len(trees)):
            if trees[j][i] > height:
                height = trees[j][i]
                treecount[j][i] = 1
        height = -1
        height2 = -1
        for k in range(len(trees)-1, -1, -1):
            if trees[k][i] > height2:
                height2 = trees[k][i]
                treecount[k][i] = 1
        strees = ""
        streecount = ""
        for a in range(len(trees)):
            strees += str(trees[a][i])
            streecount += str(treecount[a][i])
    for i, row in enumerate(trees):
        height = -1
        height2 = -1
        for j, tree in enumerate(row):
            if tree > height:
                height = tree
                treecount[i][j] = 1
        for k in range(len(row)-1, -1, -1):
            if row[k] > height2:
                height2 = row[k]
                treecount[i][k] = 1
    totalcount = 0
    for row in treecount:
        totalcount += sum(row)
    print(totalcount)