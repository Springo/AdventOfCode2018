def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d06input.txt")
coords = []
for line in lines:
    l1 = line.split(', ')
    coords.append([int(l1[0]), int(l1[1])])

grid = [[-1] * 500 for _ in range(500)]
a = 0
poss_vals = dict()
for coord in coords:
    grid[coord[0]][coord[1]] = a
    poss_vals[a] = 0
    a += 1

def mandist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def getclosest(point, plist):
    minman = -1
    minind = 0
    for i in range(len(plist)):
        man = mandist(point, plist[i])
        if minman == -1 or man < minman:
            minman = man
            minind = i

    for i in range(len(plist)):
        man = mandist(point, plist[i])
        if man == minman and i != minind:
            return None

    return minind

def gettotdist(point, plist):
    total = 0
    for i in range(len(plist)):
        total += mandist(point, plist[i])
    return total

for i in range(len(grid)):
    for j in range(len(grid)):
        closest = getclosest([i, j], coords)
        if closest is not None:
            grid[i][j] = closest

for x in range(len(grid)):
    for y in range(len(grid)):
        if grid[x][y] != -1:
            key = grid[x][y]
            if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid) - 1:
                poss_vals.pop(key, None)
            elif key in poss_vals:
                poss_vals[key] += 1

best = max(poss_vals, key=poss_vals.get)
print(poss_vals[best])

size = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if gettotdist([i,j], coords) < 10000:
            size += 1
print(size)
