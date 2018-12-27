def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d17input.txt")
#lines = readFile("test.txt")
grid = []
parsed = []
for line in lines:
    l1 = line[0]
    l2 = int(line.split(',')[0][2:])
    l3 = line.split("=")[2].split("..")
    parsed.append([l1, l2, int(l3[0]), int(l3[1])])

max_x = 0
max_y = 0
min_y = 10000
for p in parsed:
    if p[0] == 'x':
        if p[1] > max_x:
            max_x = p[1]
        if p[3] > max_y:
            max_y = p[3]
        if p[2] < min_y:
            min_y = p[2]
    if p[0] == 'y':
        if p[1] > max_y:
            max_y = p[1]
        if p[1] < min_y:
            min_y = p[1]
        if p[3] > max_x:
            max_x = p[3]

print("Min y: {}".format(min_y))
max_x += 2
max_y += 1
grid = [['.'] * max_x for _ in range(max_y)]
grid[0][500] = '+'
blocked = [[[False, False] for _2 in range(max_x)] for _ in range(max_y)]

for p in parsed:
    if p[0] == 'x':
        for a in range(p[2], p[3] + 1):
            grid[a][p[1]] = '#'
    if p[0] == 'y':
        for a in range(p[2], p[3] + 1):
            grid[p[1]][a] = '#'

def print_grid():
    for line in grid:
        for c in line:
            if c == '~':
                print('@', end=' ')
            else:
                print(c, end=' ')
        print()

entities = []
entities.append([0, 500])
grid[0][500] = '~'

done = False
total = 0
for round in range(32000):
    #i = max(0, len(entities) - 3000)
    i = 0
    if round % 1000 == 0:
        #print_grid()
        print(round)
        print(len(entities))
        print(i)
        print(total + len(entities) - min_y)
#while not done:
    new_entities = []
    while i < len(entities):
        e = entities[i]
        y = e[0]
        x = e[1]
        if y + 1 == len(grid):
            i += 1
            continue
        if grid[y + 1][x] == '.':
            new_entities.append([y+1, x])
            grid[y+1][x] = '~'
        elif grid[y + 1][x] == '#' or (blocked[y+1][x][0] and blocked[y+1][x][1]):
            if grid[y][x + 1] == '.':
                new_entities.append([y, x+1])
                grid[y][x+1] = '~'
            elif grid[y][x + 1] == '#':
                blocked[y][x][1] = True
            elif grid[y][x + 1] == '~':
                if blocked[y][x + 1][1]:
                    blocked[y][x][1] = True
            if grid[y][x - 1] == '.':
                new_entities.append([y, x - 1])
                grid[y][x-1] = '~'
            elif grid[y][x - 1] == '#':
                blocked[y][x][0] = True
            elif grid[y][x - 1] == '~':
                if blocked[y][x - 1][0]:
                    blocked[y][x][0] = True
        if blocked[y][x][0] and blocked[y][x][1]:
            entities.pop(i)
            total += 1
            i -= 1
        i += 1

    entities.extend(new_entities)

print_grid()
total += len(entities) - min_y
print(total)
