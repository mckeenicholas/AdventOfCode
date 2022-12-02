
if __name__ == "__main__":
    f = open("data2.txt")
    scores = {"X": 1, "Y":2, "Z":3}
    beats = {"A": "Y", "B": "Z", "C": "X"}
    ties = {"A":"X", "B":"Y", "C":"Z"}
    score = 0
    for line in f:
        if ties[line[0]] == line[2]:
            score += 3
        elif beats[line[0]] == line[2]:
            score += 6
        score += scores[line[2]]
        print(score)
    print(score)
