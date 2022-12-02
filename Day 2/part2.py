
if __name__ == "__main__":
    f = open("data2.txt")
    lose = {"A":"Z", "B":"X", "C":"Y"}
    scores = {"X": 1, "Y": 2, "Z": 3}
    beats = {"A": "Y", "B": "Z", "C": "X"}
    ties = {"A": "X", "B": "Y", "C": "Z"}
    score = 0
    for line in f:
        if line[2] == "Y":
            score += 3
            score += scores[ties[line[0]]]
        if line[2] == "Z":
            score += 6
            score += scores[beats[line[0]]]
        if line[2] == "X":
            score += scores[lose[line[0]]]
    print(score)