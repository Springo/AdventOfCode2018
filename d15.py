def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d15input.txt")
#lines = readFile("test.txt")
#lines = readFile("ryaninp.txt")
#lines = readFile("t6.txt")
grid = []
entities = []
ent_loc = dict()

for i in range(len(lines)):
    g_line = []
    for j in range(len(lines[i])):
        c = lines[i][j]
        if c == 'G' or c == 'E':
            entities.append([c, j, i, 200])
            ent_loc[(j, i)] = [c, 200]
            g_line.append('@')
        else:
            g_line.append(lines[i][j])
    grid.append(g_line)

def print_grid():
    for i in range(len(grid)):
        line = grid[i]
        for j in range(len(line)):
            c = line[j]
            if c == '@':
                print(ent_loc[(j, i)][0], end=' ')
            else:
                print(c, end=' ')
        print()

def man_dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def tie_break(x1, y1, x2, y2):
    if y1 < y2:
        return x1, y1
    elif y2 < y1:
        return x2, y2
    elif x1 < x2:
        return x1, y1
    else:
        return x2, y2

def multi_tie_break(p_list):
    if len(p_list) == 0:
        print("EMPTY")
    elif len(p_list) == 1:
        return p_list[0][0], p_list[0][1]
    else:
        best = p_list[0]
        for p in p_list[1:]:
            x1 = best[0]
            y1 = best[1]
            x2 = p[0]
            y2 = p[1]
            new_x1, new_x2 = tie_break(x1, y1, x2, y2)
            best = [new_x1, new_x2]
        return best[0], best[1]

def get_neigh(x, y):
    neighs = []
    if x > 0 and grid[y][x - 1] == '.':
        neighs.append([x-1, y])
    if x < len(grid[0]) - 1 and grid[y][x + 1] == '.':
        neighs.append([x+1, y])
    if y > 0 and grid[y - 1][x] == '.':
        neighs.append([x, y-1])
    if y < len(grid) - 1 and grid[y + 1][x] == '.':
        neighs.append([x, y+1])
    return neighs

def in_range(type, x, y):
    best = None
    best_hp = None
    if (x, y-1) in ent_loc and ent_loc[(x, y-1)] != 0 and ent_loc[(x, y-1)][0] != type:
        best = [x, y-1]
        best_hp = ent_loc[(x, y-1)][1]
    if (x-1, y) in ent_loc and ent_loc[(x-1, y)] != 0 and ent_loc[(x-1, y)][0] != type:
        newhp = ent_loc[(x-1, y)][1]
        if best is None or newhp < best_hp:
            best = [x-1, y]
            best_hp = newhp
    if (x+1, y) in ent_loc and ent_loc[(x+1, y)] != 0 and ent_loc[(x+1, y)][0] != type:
        newhp = ent_loc[(x + 1, y)][1]
        if best is None or newhp < best_hp:
            best = [x + 1, y]
            best_hp = newhp
    if (x, y+1) in ent_loc and ent_loc[(x, y+1)] != 0 and ent_loc[(x, y+1)][0] != type:
        newhp = ent_loc[(x, y+1)][1]
        if best is None or newhp < best_hp:
            best = [x, y+1]
            best_hp = newhp
    return best

def iter_dfs(x, y, p_list):
    p_dict = dict()
    for p in p_list:
        p_dict[(p[0], p[1])] = 1
    if (x, y) in p_dict:
        return [[x, y]]
    iter = 0
    while iter < len(grid) - 1:
        p1 = dfs(iter, x, y - 1, [[x, y]], p_dict)
        if p1 != None:
            return p1
        p2 = dfs(iter, x - 1, y, [[x, y]], p_dict)
        if p2 != None:
            return p2
        p3 = dfs(iter, x + 1, y, [[x, y]], p_dict)
        if p3 != None:
            return p3
        p4 = dfs(iter, x, y + 1, [[x, y]], p_dict)
        if p4 != None:
            return p4
        iter += 1
    return None


def dfs(iter, x, y, path, p_dict):
    path_dict = dict()
    for p in path:
        path_dict[(p[0], p[1])] = 1
    if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
        return None
    if grid[y][x] == '#' or grid[y][x] == '@':
        return None

    if iter == 0:
        if (x, y) not in p_dict:
            return None
        else:
            new_path = path[:]
            new_path.append([x,y])
            return new_path
    else:
        new_path = path[:]
        new_path.append([x,y])
        if (x, y) in p_dict:
            return new_path
        else:
            if (x, y-1) not in path_dict:
                p1 = dfs(iter - 1, x, y - 1, new_path, p_dict)
                if p1 != None:
                    return p1
            if (x-1, y) not in path_dict:
                p2 = dfs(iter - 1, x - 1, y, new_path, p_dict)
                if p2 != None:
                    return p2
            if (x+1, y) not in path_dict:
                p3 = dfs(iter - 1, x + 1, y, new_path, p_dict)
                if p3 != None:
                    return p3
            if (x, y+1) not in path_dict:
                p4 = dfs(iter - 1, x, y + 1, new_path, p_dict)
                if p4 != None:
                    return p4
            return None
            """
            sol = [p1, p2, p3, p4]
            best = -1
            best_len = -1
            for i in range(len(sol)):
                if sol[i] != None:
                    if best == -1 or len(sol[i]) < best_len:
                        best = i
                        best_len = len(sol[i])
            if best != -1:
                return sol[best]
            else:
                return None
            """

def bfs(x, y, p_list):
    p_dict = dict()
    for p in p_list:
        p_dict[(p[0], p[1])] = 1
    if (x, y) in p_dict:
        return [[x, y]]
    Q = []
    done = False
    explored = dict()
    explored[(x, y)] = 1
    solutions = []
    best_sol = 0
    if y > 0 and grid[y-1][x] == '.':
        Q.append([x, y-1, x, y-1, 1])
        explored[(x, y-1)] = 1
    if x > 0 and grid[y][x-1] == '.':
        Q.append([x-1, y, x-1, y, 1])
        explored[(x-1, y)] = 1
    if x < len(grid[0]) - 1 and grid[y][x+1] == '.':
        Q.append([x+1, y, x+1, y, 1])
        explored[(x+1, y)] = 1
    if y < len(grid) - 1 and grid[y+1][x] == '.':
        Q.append([x, y+1, x, y+1, 1])
        explored[(x, y+1)] = 1
    while len(Q) > 0:
        top = Q.pop(0)
        x_t = top[0]
        y_t = top[1]
        if (x_t, y_t) in p_dict:
            if not done:
                solutions.append([[x, y], [top[2], top[3]], [x_t, y_t]])
                done = True
                best_sol = top[4]
            else:
                if top[4] == best_sol:
                    solutions.append([[x, y], [top[2], top[3]], [x_t, y_t]])
        if not done:
            if y_t > 0 and (x_t, y_t - 1) not in explored and grid[y_t - 1][x_t] == '.':
                Q.append([x_t, y_t - 1, top[2], top[3], top[4] + 1])
                explored[(x_t, y_t - 1)] = 1
            if x_t > 0 and (x_t - 1, y_t) not in explored and grid[y_t][x_t - 1] == '.':
                Q.append([x_t - 1, y_t, top[2], top[3], top[4] + 1])
                explored[(x_t - 1, y_t)] = 1
            if x_t < len(grid[0]) - 1 and (x_t + 1, y_t) not in explored and grid[y_t][x_t + 1] == '.':
                Q.append([x_t + 1, y_t, top[2], top[3], top[4] + 1])
                explored[(x_t + 1, y_t)] = 1
            if y_t < len(grid) - 1 and (x_t, y_t + 1) not in explored and grid[y_t + 1][x_t] == '.':
                Q.append([x_t, y_t + 1, top[2], top[3], top[4] + 1])
                explored[(x_t, y_t + 1)] = 1
    if len(solutions) > 0:
        points = []
        for s in solutions:
            points.append(s[2])
        x_best, y_best = multi_tie_break(points)
        for s in solutions:
            if x_best == s[2][0] and y_best == s[2][1]:
                return [s[0], s[1]]
    return None


def get_closest_spot(type, x, y):
    poss = []
    for e in entities:
        if e[0] != type:
            neigh = get_neigh(e[1], e[2])
            for n in neigh:
                poss.append(n)
    """
    s_dist = -1
    s_list = []
    for p in poss:
        dist = man_dist(x, y, p[0], p[1])
        if s_dist == -1 or dist < s_dist:
            if dist == s_dist:
                s_list.append([p[0], p[1]])
            else:
                s_dist = dist
                s_list = []
                s_list.append([p[0], p[1]])
    return multi_tie_break(s_list)
    """
    return bfs(x, y, poss)

def check_done():
    type = entities[0][0]
    total = 0
    for e in entities:
        if e[0] != type:
            return None
        total += e[3]
    return total

p2_done = False
elf_att = 3
while not p2_done:
    grid = []
    entities = []
    ent_loc = dict()

    for i in range(len(lines)):
        g_line = []
        for j in range(len(lines[i])):
            c = lines[i][j]
            if c == 'G' or c == 'E':
                entities.append([c, j, i, 200])
                ent_loc[(j, i)] = [c, 200]
                g_line.append('@')
            else:
                g_line.append(lines[i][j])
        grid.append(g_line)

    num_elves = 0
    for e in entities:
        if e[0] == 'E':
            num_elves += 1

    turns = 0
    elf_att += 1
    print(elf_att)
    done = False
    while not done:
    #for _ in range(10):
        #turns += 1
        entities = sorted(entities, key=lambda a: a[1])
        entities = sorted(entities, key=lambda a: a[2])
        #print(entities)
        i = 0
        while i < len(entities):
            e = entities[i]
            #print(e)
            type = e[0]
            x = e[1]
            y = e[2]
            health = e[3]
            enemy = in_range(type, x, y)
            if enemy is None:
                path = get_closest_spot(type, x, y)
                if path is not None:
                    next_step = path[1]
                    newx = next_step[0]
                    newy = next_step[1]
                    entities[i] = [type, newx, newy, health]
                    grid[y][x] = '.'
                    grid[newy][newx] = '@'
                    ent_loc[(x, y)] = 0
                    ent_loc[(newx, newy)] = [type, health]
                    enemy = in_range(type, newx, newy)
                    #print("{} {}".format(newx, newy))
            if enemy is not None:
                enx = enemy[0]
                eny = enemy[1]
                for j in range(len(entities)):
                    e2 = entities[j]
                    if e2[1] == enx and e2[2] == eny:
                        if (e2[0] == 'E' and e2[3] <= 3) or (e2[0] == 'G' and e2[3] <= elf_att):
                            grid[eny][enx] = '.'
                            ent_loc[(enx, eny)] = 0
                            entities.pop(j)
                            if j < i:
                                i -= 1
                            final = check_done()
                            if final is not None:
                                done = True
                                if i == len(entities) - 1:
                                    turns += 1
                                entities = sorted(entities, key=lambda a: a[1])
                                entities = sorted(entities, key=lambda a: a[2])
                                if entities[0][0] == 'E' and len(entities) == num_elves:
                                    p2_done = True
                                print(entities)
                                print(final)
                                print(turns)
                                print(final * turns)
                                print_grid()
                        else:
                            entities[j] = [e2[0], e2[1], e2[2], e2[3] - 3]
                            ent_loc[(e2[1], e2[2])] = [e2[0], e2[3] - 3]
                        break
            #print_grid()
            if done:
                break
            i += 1
        if done:
            break
        turns += 1
        #print(entities)
