def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d13input.txt")
#lines = readFile("test.txt")
grid = []
c_list = []
locs = dict()
for y in range(len(lines)):
    line = lines[y]
    g_line = []
    for x in range(len(line)):
        c = line[x]
        if c == '>':
            g_line.append('-')
            c_list.append([y, x, 0, 0])
            locs[(y, x)] = 1
        elif c == '<':
            g_line.append('-')
            c_list.append([y, x, 2, 0])
            locs[(y, x)] = 1
        elif c == 'v':
            g_line.append('|')
            c_list.append([y, x, 1, 0])
            locs[(y, x)] = 1
        elif c == '^':
            g_line.append('|')
            c_list.append([y, x, 3, 0])
            locs[(y, x)] = 1
        else:
            g_line.append(c)
    grid.append(g_line)

done = False
while not done:
    c_list = sorted(c_list, key=lambda a: a[1])
    c_list = sorted(c_list, key=lambda a: a[0])
    i = 0
    while i < len(c_list):
        if i < 0:
            print("NOOOOOO")
        pair = c_list[i]
        y = pair[0]
        x = pair[1]
        dir = pair[2]
        turn = pair[3]
        locs[(y, x)] = 0
        if dir == 0:
            x = x + 1
            if (y, x) in locs and locs[(y, x)] == 1:
                print("COLLISION")
                print("{},{}".format(x, y))
                print(c_list)
                print(c_list.pop(i))
                for j in range(len(c_list)):
                    newy = c_list[j][0]
                    newx = c_list[j][1]
                    if newy == y and newx == x:
                        print(c_list.pop(j))
                        if j < i:
                            i -= 1
                        break
                print(c_list)
                locs[(y, x)] = 0
                continue
            if grid[y][x] == '/':
                dir = 3
            elif grid[y][x] == '\\':
                dir = 1
            elif grid[y][x] == '+':
                if turn == 0:
                    dir = 3
                    turn = 1
                elif turn == 1:
                    turn = 2
                elif turn == 2:
                    dir = 1
                    turn = 0
        elif dir == 1:
            y = y + 1
            if (y, x) in locs and locs[(y, x)] == 1:
                print("COLLISION")
                print("{},{}".format(x, y))
                print(c_list)
                print(c_list.pop(i))
                for j in range(len(c_list)):
                    newy = c_list[j][0]
                    newx = c_list[j][1]
                    if newy == y and newx == x:
                        print(c_list.pop(j))
                        if j < i:
                            i -= 1
                        break
                locs[(y, x)] = 0
                print(c_list)
                continue
            if grid[y][x] == '/':
                dir = 2
            elif grid[y][x] == '\\':
                dir = 0
            elif grid[y][x] == '+':
                if turn == 0:
                    dir = 0
                    turn = 1
                elif turn == 1:
                    turn = 2
                elif turn == 2:
                    dir = 2
                    turn = 0
        elif dir == 2:
            x = x - 1
            if (y, x) in locs and locs[(y, x)] == 1:
                print("COLLISION")
                print("{},{}".format(x, y))
                print(c_list)
                print(c_list.pop(i))
                for j in range(len(c_list)):
                    newy = c_list[j][0]
                    newx = c_list[j][1]
                    if newy == y and newx == x:
                        print(c_list.pop(j))
                        if j < i:
                            i -= 1
                        break
                locs[(y, x)] = 0
                print(c_list)
                continue
            if grid[y][x] == '/':
                dir = 1
            elif grid[y][x] == '\\':
                dir = 3
            elif grid[y][x] == '+':
                if turn == 0:
                    dir = 1
                    turn = 1
                elif turn == 1:
                    turn = 2
                elif turn == 2:
                    dir = 3
                    turn = 0
        elif dir == 3:
            y = y - 1
            if (y, x) in locs and locs[(y, x)] == 1:
                print("COLLISION")
                print("{},{}".format(x, y))
                print(c_list)
                print(c_list.pop(i))
                for j in range(len(c_list)):
                    newy = c_list[j][0]
                    newx = c_list[j][1]
                    if newy == y and newx == x:
                        print(c_list.pop(j))
                        if j < i:
                            i -= 1
                        break
                locs[(y, x)] = 0
                print(c_list)
                continue
            if grid[y][x] == '/':
                dir = 0
            elif grid[y][x] == '\\':
                dir = 2
            elif grid[y][x] == '+':
                if turn == 0:
                    dir = 2
                    turn = 1
                elif turn == 1:
                    turn = 2
                elif turn == 2:
                    dir = 0
                    turn = 0
        else:
            print("AAAAAA")
        locs[(y, x)] = 1
        new_pair = [y, x, dir, turn]
        c_list[i] = new_pair
        i += 1
    if len(c_list) < 2:
        print("FINAL:")
        print("{},{}".format(c_list[0][1], c_list[0][0]))
        done = True
