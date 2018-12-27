def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d07input.txt")
pairs = []
for line in lines:
    l1 = line.split(' ')
    pairs.append([l1[1], l1[7]])

adjlist = dict()
startlist = dict()
revlist = dict()
for pair in pairs:
    if pair[0] not in adjlist:
        adjlist[pair[0]] = []
    if pair[1] not in revlist:
        revlist[pair[1]] = []
    adjlist[pair[0]].append(pair[1])
    revlist[pair[1]].append(pair[0])
    if pair[0] not in startlist:
        startlist[pair[0]] = 1
    startlist[pair[1]] = 0

q = []
final = ""
templist = []
done = dict()
finished = dict()
for key in startlist:
    if startlist[key] == 1:
        templist.append(key)
        done[key] = 1

templist = sorted(templist)
for x in templist:
    q.append(x)

def isvalid(val):
    if val not in revlist:
        return True
    for x in revlist[val]:
        if x not in finished:
            return False
    return True

while len(q) > 0:
    q = sorted(q)
    ind = 0
    for i in range(len(q)):
        if isvalid(q[i]):
            ind = i
            break
    cur = q.pop(i)
    finished[cur] = 1
    final = final + cur
    if cur in adjlist:
        templist = sorted(adjlist[cur])
        for x in templist:
            if x not in done:
                done[x] = 1
                q.append(x)

print(final)

ready = []
workers = [0, 0, 0, 0, 0]
#workers = [0, 0]
for c in final:
    if c not in revlist:
        ready.append(c)

"""
def nowready(fin_list, val):
    for x in revlist[val]:
        if x not in fin_list:
            return False
    return True

fin_list = dict()
next_ready = ready
while len(next_ready) > 0:
    ready = next_ready
    next_ready = []
    while len(ready) > 0:
        cur = ready.pop(0)
        fin_list[cur] = 0
        #workers[0] += 60 + ord(cur) - 64
        workers[0] += ord(cur) - 64
        workers = sorted(workers)
        for c in final:
            if c not in fin_list and c not in ready and nowready(fin_list, c):
                next_ready.append(c)
        ready = sorted(ready)
        print(workers)

print(workers[-1])
"""

def nowready(fin_list, val):
    for x in revlist[val]:
        if x not in fin_list or fin_list[x] != -1:
            return False
    return True

time = 0
fin_list = dict()
job_list = dict()
while sum(workers) > 0 or len(ready) > 0:
    if len(ready) == 0:
        time += 1
        for i in range(len(workers)):
            if workers[i] > 0:
                workers[i] -= 1
                if workers[i] == 0:
                    fin_list[job_list[i]] = -1
                    for c in final:
                        if c not in ready and c not in fin_list and nowready(fin_list, c):
                            ready.append(c)
                    ready = sorted(ready)
    else:
        cur = ready.pop(0)
        while cur not in fin_list:
            for i in range(len(workers)):
                if workers[i] == 0:
                    workers[i] = 60 + ord(cur) - 64
                    fin_list[cur] = i
                    job_list[i] = cur
                    break
            if cur not in fin_list:
                time += 1
                for i in range(len(workers)):
                    if workers[i] > 0:
                        workers[i] -= 1
                        if workers[i] == 0:
                            fin_list[job_list[i]] = -1
                            for c in final:
                                if c not in ready and c not in fin_list and nowready(fin_list, c):
                                    ready.append(c)
                            ready = sorted(ready)

print(time)
