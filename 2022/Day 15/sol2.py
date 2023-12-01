f = open("data15.txt")
data = {}
empty = set()
for line in f:
    items = line.split()
    sensor = (int(items[2][2:-1]),int(items[3][2:-1]))
    beacon = (int(items[8][2:-1]),int(items[9][2:]))
    data[sensor] = beacon
sensors = list(data.keys())
for i in range(len(sensors)):
    for j in range(i + 1, len(sensors)):
        dist1 = abs(sensors[i][0] - data[sensors[i]][0]) + abs(sensors[i][1] - data[sensors[i]][1])
        dist2 = abs(sensors[j][0] - data[sensors[j]][0]) + abs(sensors[j][1] - data[sensors[j]][1])
        if abs(sensors[i][0] - sensors[j][0] + sensors[i][1] - sensors[j][1]) == dist1 + dist2 + 2:
            stepx = 1
            stepy = 1
            if sensors[i][0] - sensors[j][0] > 0:
                stepx = -1
            if sensors[i][1] - sensors[j][1] < 0:
                stepy = -1
            for x in range(dist1 + 2):
                location = (sensors[i][0] + stepx * x, sensors[i][1] - stepy * (dist1 - x + 1))
                if abs(location[0] - sensors[j][0]) <= dist2 + 1 and abs(location[1] - sensors[j][1]) <= dist2 + 1:
                    found = True
                    for sensor in sensors:
                        distance = abs(sensor[0] - data[sensor][0]) + abs(sensor[1] - data[sensor][1])
                        if abs(sensor[0] - location[0]) + abs(sensor[1] - location[1]) <= distance:
                            found = False
                    if found:
                        print(location[0] * 4000000 + location[1])
                        exit()