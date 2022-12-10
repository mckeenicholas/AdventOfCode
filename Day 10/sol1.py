f = open("data10.txt")
value = 1
cycle = 1
important_cycles = [20, 60, 100, 140, 180, 220]
value_sum = 0
for line in f:
    if line.strip() == "noop":
        if cycle in important_cycles:
            value_sum += (cycle * value)
        cycle += 1
    else:
        num = int(line.strip()[4:])
        if cycle in important_cycles:
            value_sum += (cycle * value)
        cycle += 1
        if cycle in important_cycles:
            value_sum += (cycle * value)
        cycle += 1
        value += num
print(value_sum)
