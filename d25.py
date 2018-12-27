def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d25input.txt")

def man_dist(p1, p2):
    total = 0
    for i in range(len(p1)):
        total += abs(p1[i] - p2[i])
    return total

stars = []
for line in lines:
    l1 = line.split(",")
    stars.append([int(a) for a in l1])

graph = dict()
found = dict()

for i in range(len(stars)):
    s1 = stars[i]
    if i not in graph:
        graph[i] = []
    found[i] = False
    for j in range(len(stars)):
        s2 = stars[j]
        if i != j:
            if man_dist(s1, s2) <= 3:
                graph[i].append(j)


def find_not_done(found):
    for key in found:
        if not found[key]:
            return key
    return None

done = False
consts = 0
while not done:
    cur = find_not_done(found)
    if cur is None:
        done = True
    else:
        q = [cur]
        found[cur] = True
        consts += 1
        while len(q) > 0:
            pos = q.pop(0)
            star = stars[pos]
            for neigh in graph[pos]:
                if not found[neigh]:
                    found[neigh] = True
                    q.append(neigh)
print(consts)

