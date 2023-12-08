import re
from collections import defaultdict

d = defaultdict(int)
for i, line in enumerate(open("data.txt")):
    d[i] += 1
    nums = [int(num.strip()) for num in re.findall(r"\d+", line)]
    for j in range(len(set(nums[1:11]) & set(nums[11:]))):
        d[i + j + 1] += d[i]
print(sum(d.values()))
