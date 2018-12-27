def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d18input.txt")
grid = []
for line in lines:
    g_line = [c for c in line]
    grid.append(g_line)

def check_neighb(y, x):
    trees = 0
    lumbs = 0
    opens = 0
    vals = []
    if x > 0:
        vals.append(grid[y][x - 1])
        if y > 0:
            vals.append(grid[y - 1][x - 1])
        if y < len(grid) - 1:
            vals.append(grid[y + 1][x - 1])
    if y > 0:
        vals.append(grid[y - 1][x])
    if y < len(grid) - 1:
        vals.append(grid[y + 1][x])
    if x < len(grid[0]) - 1:
        vals.append(grid[y][x + 1])
        if y > 0:
            vals.append(grid[y - 1][x + 1])
        if y < len(grid) - 1:
            vals.append(grid[y + 1][x + 1])

    for v in vals:
        if v == '.':
            opens += 1
        if v == '#':
            lumbs += 1
        if v == '|':
            trees += 1
    return trees, lumbs, opens

def iter_once():
    global grid
    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            trees, lumbs, opens = check_neighb(y, x)
            if grid[y][x] == '.':
                if trees >= 3:
                    new_grid[y][x] = '|'
                else:
                    new_grid[y][x] = '.'
            elif grid[y][x] == '|':
                if lumbs >= 3:
                    new_grid[y][x] = '#'
                else:
                    new_grid[y][x] = '|'
            elif grid[y][x] == '#':
                if lumbs >= 1 and trees >= 1:
                    new_grid[y][x] = '#'
                else:
                    new_grid[y][x] = '.'
    grid = new_grid

def get_val():
    global grid
    trees = 0
    lumbs = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '#':
                lumbs += 1
            elif grid[y][x] == '|':
                trees += 1

    return trees * lumbs

def print_grid():
    for line in grid:
        for c in line:
            print(c, end=' ')
        print()

print("Resource: {}".format((1000000000 - 551) % 28))

done = False
#while not done:
for i in range(10000):
    iter_once()
    val = get_val()
    if i > 551:
        print(val)
        print_grid()
    if val == 210160:
        print(i)

