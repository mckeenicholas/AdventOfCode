class Monkey:
    def __init__(self):
        self.operation = ""
        self.value = 0
        self.items = []
        self.test = 0
        self.true = 0
        self.false = 0
        self.inspections = 0


f = open("data11.txt")
monkeys = {}
line = f.readline().strip()
while line != "":
    if "Monkey" in line:
        num = int(line[7])
        m = Monkey()
        line = f.readline().strip()
        items = line[16:].split(",")
        for item in items:
            m.items.append(int(item))
        line = f.readline().strip()
        m.operation = line[21]
        if line[23:] == "old":
            m.operation = "x"
        else:
            m.value = int(line[23:])
        line = f.readline().strip()
        m.test = int(line[19:])
        line = f.readline().strip()
        m.true = int(line[25:])
        line = f.readline().strip()
        m.false = int(line[26:])
        monkeys[num] = m
    line = f.readline()

for _ in range(20):
    for monkey in monkeys.values():
        for j in range(len(monkey.items)):
            if monkey.operation == "x":
                monkey.items[j] = monkey.items[j] * monkey.items[j]
            elif monkey.operation == "*":
                monkey.items[j] = monkey.items[j] * monkey.value
            elif monkey.operation == "+":
                monkey.items[j] = monkey.items[j] + monkey.value
            monkey.items[j] = monkey.items[j] // 3
            if monkey.items[j] % monkey.test == 0:
                monkeys[monkey.true].items.append(monkey.items[j])
            else:
                monkeys[monkey.false].items.append(monkey.items[j])
            monkey.inspections += 1
        monkey.items.clear()
throws = []
for monkey in monkeys.values():
    throws.append(monkey.inspections)
throws.sort(reverse=True)
print(throws[0] * throws[1])