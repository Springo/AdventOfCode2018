def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d10input.txt")
poslist = []
vellist = []
for line in lines:
    l1 = line.split("<")
    l2 = l1[1].split(">")
    l3 = l2[0].split(',')
    pos = [int(l3[0]), int(l3[1])]
    l4 = l1[2].split(',')
    vel = [int(l4[0]), int(l4[1][:-1])]
    poslist.append(pos)
    vellist.append(vel)

def print_grid():
    min_x = min(poslist, key=lambda x: x[0])[0]
    min_y = min(poslist, key=lambda x: x[1])[1]
    max_x = max(poslist, key=lambda x: x[0])[0]
    max_y = max(poslist, key=lambda x: x[1])[1]
    width = max_x - min_x + 1
    length = max_y - min_y + 1
    if width < 100 and length < 100:
        grid = [[' '] * width for _ in range(length)]
        for pos in poslist:
            x = pos[0] - min_x
            y = pos[1] - min_y
            grid[y][x] = 'X'
        for line in grid:
            for c in line:
                print(c, end='')
            print()
        return True
    else:
        return False

def iter_pos():
    for i in range(len(poslist)):
        x = poslist[i][0]
        y = poslist[i][1]
        dx = vellist[i][0]
        dy = vellist[i][1]
        poslist[i] = [x + dx, y + dy]

counter = 0
done = False
i = 0
while not done:
    iter_pos()
    i += 1
    if print_grid():
        print("-------------------")
        counter += 1
    if counter > 4:
        done = True
print(i)
