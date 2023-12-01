import re

f = open("data.txt")
total = 0
for line in f:
    res = [int(num) for num in re.findall(r'\d', line)]
    total += 10 * res[0] + res[-1]
print(total)