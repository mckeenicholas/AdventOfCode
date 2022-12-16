f = open("data15.txt")
data = {}
empty = set()
for line in f:
    items = line.split()
    sensor = (int(items[2][2:-1]),int(items[3][2:-1]))
    beacon = (int(items[8][2:-1]),int(items[9][2:]))
    data[sensor] = beacon
beacons = data.values()
left, right = 0, 0
for sensor in data.keys():
    distance = abs(sensor[0] - data[sensor][0]) + abs(sensor[1] - data[sensor][1])
    hdist = abs(2000000 - sensor[1])
    if distance >= hdist:
        left = min(left, sensor[0] + hdist - distance)
        right = max(right, sensor[0] - hdist + distance)
print(right - left)