import re

total = 0
f = open("data.txt")
digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in f:
    res = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    nums = [digits.index(i) if i in digits else int(i) for i in res]
    total += 10 * nums[0] + nums[-1]
print(total)