from random import shuffle, randint

def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

def man_dist(p1, p2):
    total = 0
    for i in range(len(p1)):
        total += abs(p2[i] - p1[i])
    return total

lines = readFile("d23input.txt")
#lines = readFile("test.txt")
bots = []
for line in lines:
    l1 = line.split(", ")
    a = l1[0][5:-1].split(',')
    b = l1[1][2:]
    bots.append([int(a[0]), int(a[1]), int(a[2]), int(b)])

best = max(bots, key=lambda a: a[3])
best_ind = bots.index(best)
count = 0
for b in bots:
    if man_dist(b[0:3], best[0:3]) < best[3]:
        count += 1
print(count)

""" DOESN'T WORK
intersects = dict()
intersects[1] = [[b] for b in bots]
for i in range(2, len(bots)):
    print(i)
    intersects[i] = []
    for p_i in intersects[i - 1]:
        for p in bots:
            if p not in p_i:
                add = True
                for p_2 in p_i:
                    dist = man_dist(p[0:3], p_2[0:3])
                    if dist > p[3] + p_2[3]:
                        add = False
                if add:
                    p_new = p_i[:]
                    p_new.append(p)
                    intersects[i].append(p_new)
"""


def convert_rect(p):
    x1 = p[0] - p[3]
    x2 = p[0] + p[3]
    y1 = p[1] - p[3]
    y2 = p[1] + p[3]
    z1 = p[2] - p[3]
    z2 = p[2] + p[3]
    return [x1, x2, y1, y2, z1, z2]

def get_overlap(p1, p2):
    x1 = max(p1[0], p2[0])
    x2 = min(p1[1], p2[1])
    y1 = max(p1[2], p2[2])
    y2 = min(p1[3], p2[3])
    z1 = max(p1[4], p2[4])
    z2 = min(p1[5], p2[5])
    if x2 < x1 or y2 < y1 or z2 < z1:
        return None
    return [x1, x2, y1, y2, z1, z2]

"""
rects = []
for b in bots:
    rects.append(convert_rect(b))
"""

"""
intersects = dict()
intersects[1] = [r for r in rects]
storage = dict()
storage[1] = dict()
for r in rects:
    storage[1][tuple(r)] = [r]
for i in range(2, len(bots)):
    print(i)
    intersects[i] = []
    storage[i] = dict()
    for p_i in intersects[i - 1]:
        for p in rects:
            if p not in storage[i - 1][tuple(p_i)]:
                overlap = get_overlap(p, p_i)
                if overlap is not None:
                    used = storage[i-1][tuple(p_i)][:]
                    used.append(p)
                    intersects[i].append(overlap)
                    storage[i][tuple(overlap)] = used
print(intersects[1000])
"""

"""
def attempt(rects):
    samp = rects[:]
    shuffle(samp)
    count = 1
    region = samp[0]
    for i in range(1, len(samp)):
        print(samp[i])
        print(region)
        overlap = get_overlap(samp[i], region)
        if overlap is not None:
            print("overlap!")
            count += 1
            region = overlap
    return region, count

results = []
for i in range(1):
    results.append(attempt(rects))

best = max(results, key=lambda a:a[1])
print(best)
print(man_dist([0,0,0], [best[0][0], best[0][2], best[0][4]]))
"""

def count_in_range(p, points):
    count = 0
    for p_i in points:
        if man_dist(p, p_i[0:3]) <= p_i[3]:
            count += 1
    return count

def intersects(p1, p2):
    dist = man_dist(p1[0:3], p2[0:3])
    if dist <= p1[3] + p2[3]:
        return True
    return False



"""
best = 0
best_p = None
for i in range(1):
    x = randint(min_x, max_x)
    y = randint(min_y, max_y)
    z = randint(min_z, max_z)
    p = [x, y, z]
    count = count_in_range(p, bots)
    if count > best:
        best = count
        best_p = p

print(best)
print(best_p)
"""

def attempt(points):
    samp = points[:]
    shuffle(samp)
    count = 1
    group = [samp[0]]
    for i in range(1, len(samp)):
        add = True
        for p in group:
            if not intersects(p, samp[i]):
                add = False
        if add:
            group.append(samp[i])
            count += 1

    return group, count

results = []
for i in range(5):
    results.append(attempt(bots))

best = max(results, key=lambda a:a[1])
print(best[1])

rects = []
for p in best[0]:
    rects.append(convert_rect(p))
overlap = rects[0]
for r in rects[1:]:
    overlap = get_overlap(overlap, r)
print(overlap)

#start_x = (overlap[1] - overlap[0]) // 2 + overlap[0]
#start_y = (overlap[3] - overlap[2]) // 2 + overlap[2]
#start_z = (overlap[5] - overlap[4]) // 2 + overlap[4]
min_x = overlap[0]
min_y = overlap[2]
min_z = overlap[4]
max_x = overlap[1]
max_y = overlap[3]
max_z = overlap[5]
#start = [start_x, start_y, start_z]
results = []
for i in range(10000):
    point = [randint(min_x, max_x), randint(min_y, max_y), randint(min_z, max_z)]
    results.append([point, count_in_range(point, bots)])
best = max(results, key=lambda a: a[1])
print(best)

def converge(lr, point, threshold):
    cur = point
    cur_best = threshold
    done = False
    while not done:
        news = []
        new_x = cur[:]
        if new_x[0] > 0:
            new_x[0] -= lr
            count = count_in_range(new_x, bots)
            news.append([new_x, count])
        elif new_x[0] < 0:
            new_x[0] += lr
            count = count_in_range(new_x, bots)
            news.append([new_x, count])
        new_y = cur[:]
        if new_y[1] > 0:
            new_y[1] -= lr
            count = count_in_range(new_y, bots)
            news.append([new_y, count])
        elif new_y[1] < 0:
            new_y[1] += lr
            count = count_in_range(new_y, bots)
            news.append([new_y, count])
        new_z = cur[:]
        if new_z[2] > 0:
            new_z[2] -= lr
            count = count_in_range(new_z, bots)
            news.append([new_z, count])
        elif new_z[2] < 0:
            new_z[2] += lr
            count = count_in_range(new_z, bots)
            news.append([new_z, count])
        new_best = max(news, key = lambda a: a[1])
        if new_best[1] < cur_best:
            done = True
        else:
            cur_best = new_best[1]
            cur = new_best[0]
    return cur, cur_best


cur_best = best[1]
cur = best[0]
lr = 1000
for i in range(4):
    print(cur)
    print(cur_best)
    cur, cur_best = converge(lr, cur, cur_best)
    lr /= 10

print(cur)
print(cur_best)
print(man_dist([0,0,0], cur))
