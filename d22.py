depth = 11817
#target = [9, 751]
#depth = 510


total = 0
grid = [[0] * 100 for _ in range(1000)]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if i == 0:
            geo_ind = j * 16807
        elif j == 0:
            geo_ind = i * 48271
        else:
            geo_ind = grid[i-1][j] * grid[i][j-1]
        grid[i][j] = (geo_ind + depth) % 20183
grid[0][0] = 0
grid[751][9] = 0
for i in range(752):
    for j in range(10):
        total += grid[i][j] % 3
print(total)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        grid[i][j] = grid[i][j] % 3

def get_neighb(y, x):
    neighb = []
    if y > 0:
        neighb.append([y-1, x])
    if x > 0:
        neighb.append([y, x-1])
    if y < 999:
        neighb.append([y+1, x])
    if x < 99:
        neighb.append([y, x+1])
    return neighb

dp = [[[-1 for _ in range(3)] for _2 in range(100)] for _3 in range(1000)]
fixed = [[[False for _ in range(3)] for _2 in range(100)] for _3 in range(1000)]
found = [[[False for _ in range(3)] for _2 in range(100)] for _3 in range(1000)]
q = dict()
q[(0,0,2)] = 0
found[0][0][2] = True

while len(q) > 0:
    cur = min(q, key=q.get)
    val = q[cur]
    q.pop(cur, None)
    y = cur[0]
    x = cur[1]
    tool = cur[2]
    fixed[y][x][tool] = True
    dp[y][x][tool] = val
    neighb = get_neighb(y, x)
    for n in neighb:
        y_n = n[0]
        x_n = n[1]
        add = False
        if tool == 0:
            if (grid[y_n][x_n] == 1 or grid[y_n][x_n] == 2) and not fixed[y_n][x_n][tool]:
                add = True
        elif tool == 1:
            if (grid[y_n][x_n] == 0 or grid[y_n][x_n] == 1) and not fixed[y_n][x_n][tool]:
                add = True
        elif tool == 2:
            if (grid[y_n][x_n] == 0 or grid[y_n][x_n] == 2) and not fixed[y_n][x_n][tool]:
                add = True
        if add:
            if (y_n, x_n, tool) not in q:
                q[(y_n, x_n, tool)] = val + 1
            else:
                if q[(y_n, x_n, tool)] > val + 1:
                    q[(y_n, x_n, tool)] = val + 1

    if grid[y][x] == 0:
        if tool == 1 and not fixed[y][x][2]:
            if (y, x, 2) not in q:
                q[(y, x, 2)] = val + 7
            else:
                if q[(y, x, 2)] > val + 7:
                    q[(y, x, 2)] = val + 7
        if tool == 2 and not fixed[y][x][1]:
            if (y, x, 1) not in q:
                q[(y, x, 1)] = val + 7
            else:
                if q[(y, x, 1)] > val + 7:
                    q[(y, x, 1)] = val + 7

    if grid[y][x] == 1:
        if tool == 1 and not fixed[y][x][0]:
            if (y, x, 0) not in q:
                q[(y, x, 0)] = val + 7
            else:
                if q[(y, x, 0)] > val + 7:
                    q[(y, x, 0)] = val + 7
        if tool == 0 and not fixed[y][x][1]:
            if (y, x, 1) not in q:
                q[(y, x, 1)] = val + 7
            else:
                if q[(y, x, 1)] > val + 7:
                    q[(y, x, 1)] = val + 7

    if grid[y][x] == 2:
        if tool == 0 and not fixed[y][x][2]:
            if (y, x, 2) not in q:
                q[(y, x, 2)] = val + 7
            else:
                if q[(y, x, 2)] > val + 7:
                    q[(y, x, 2)] = val + 7
        if tool == 2 and not fixed[y][x][0]:
            if (y, x, 0) not in q:
                q[(y, x, 0)] = val + 7
            else:
                if q[(y, x, 0)] > val + 7:
                    q[(y, x, 0)] = val + 7

def print_grid(y, x):
    for i in range(y):
        for j in range(x):
            if grid[i][j] == 0:
                print('.', end=' ')
            elif grid[i][j] == 1:
                print('~', end=' ')
            elif grid[i][j] == 2:
                print('|', end=' ')
        print()

print(dp[751][9][2])

