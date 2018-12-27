inp = 3214

def computePower(x, y):
    global inp
    rack_id = x + 10
    power = rack_id * y
    power += inp
    power *= rack_id
    h_dig = (power // 100) % 10
    power = h_dig - 5
    return power

def getPowerGrid(x, y, span, grid):
    power = 0
    for i in range(span):
        for j in range(span):
            power += grid[y + i][x + j]
    return power

def getPowerRel(x, y, span, grid, sumgrid):
    power = sumgrid[y][x]
    for i in range(span):
        power += grid[y + span - 1][x + i]
        power += grid[y + i][x + span - 1]
    power -= grid[y + span - 1][x + span - 1]
    return power

grid = [[0] * 300 for _ in range(300)]
for y in range(300):
    for x in range(300):
        grid[y][x] = computePower(x, y)

bestx = 0
besty = 0
bestpower = -100
bestspan = 1
for y in range(300):
    for x in range(300):
        power = grid[y][x]
        if power > bestpower:
            bestx = x
            besty = y
            bestpower = power

pastgrid = grid
for span in range(2, 70):
    print(span)
    newgrid = [[0] * 300 for _ in range(300)]
    for y in range(301 - span):
        for x in range(301 - span):
            power = getPowerRel(x, y, span, grid, pastgrid)
            newgrid[y][x] = power
            if power > bestpower:
                bestx = x
                besty = y
                bestpower = power
                bestspan = span
    pastgrid = newgrid

print("{},{},{}".format(bestx, besty, bestspan))
