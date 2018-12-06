def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d03input.txt")
rects = []
ids = []
for line in lines:
    l1 = line.split(" ")
    l2 = l1[2].split(",")
    x = int(l2[0])
    y = int(l2[1][:-1])
    l3 = l1[3].split("x")
    w = int(l3[0])
    l = int(l3[1])
    id = int(l1[0][1:])
    rects.append([x, y, w, l, id])

grid = [[0] * 1000 for _ in range(1000)]

for r in rects:
    for i in range(r[0], r[0] + r[2]):
        for j in range(r[1], r[1] + r[3]):
            grid[i][j] += 1

count = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] >= 2:
            count += 1

print(count)

for i in range(len(rects)):
    r = rects[i]
    good_rect = True
    for i in range(r[0], r[0] + r[2]):
        for j in range(r[1], r[1] + r[3]):
            if grid[i][j] != 1:
                good_rect = False

    if good_rect:
        print(r[4])

for row in grid:
    print(row)
