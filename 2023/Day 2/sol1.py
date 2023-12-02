import re

threshold = {'red': 12, 'blue': 14, 'green': 13}
total = 0
for x, line in enumerate(open("data.txt")):
    res = re.findall(r'(\d+) (red|blue|green)', line)
    if not any(int(num) > threshold[color] for num, color in res):
        total += x + 1
print(total)
