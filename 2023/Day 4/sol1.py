import re

total = 0
for line in open("data.txt"):
    nums = [int(num.strip()) for num in re.findall(r"\d+", line)]
    total += 2**(len(set(nums[1:11]) & set(nums[11:])) - 1) if (len(set(nums[1:11]) & set(nums[11:]))) else 0
print(total)