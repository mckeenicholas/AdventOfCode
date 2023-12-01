
def parse(input):
    output = []
    x = 0
    while x < len(input):
        if input[x] == "[":
            end = x
            count = 1
            for char in input[x + 1:]:
                end += 1
                if char == "[":
                    count += 1
                elif char == "]":
                    count -= 1
                if count == 0:
                    break
            output.append(parse(input[x + 1:end]))
            x = end
        elif 48 <= ord(input[x]) <= 57:
            if x + 1 < len(input) and 48 <= ord(input[x + 1]) <= 57:
                output.append(int(input[x:x+2]))
                x += 1
            else:
                output.append(int(input[x]))
        x += 1
    return output


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        else:
            return left < right
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left], right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])
    else:
        for i in range(min(len(left), len(right))):
            if compare(left[i], right[i]) is not None:
                return compare(left[i], right[i])
        if len(left) == len(right):
            return None
        else:
            return len(left) < len(right)


f = open("data13.txt")
total = 0
pairs = [parse(packet) for packet in f.read().split("\n\n")]
for x, pair in enumerate(pairs):
    if compare(pair[0], pair[1]):
        total += x + 1
print(total)
