def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d02input.txt")
twos = 0
threes = 0
for line in lines:
    counter = dict()
    for c in line:
        if c not in counter:
            counter[c] = 0
        counter[c] += 1
    for c in counter:
        if counter[c] == 2:
            twos += 1
            break
    for c in counter:
        if counter[c] == 3:
            threes += 1
            break

print(twos * threes)

def checkdiff(l1, l2):
    diff = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            diff += 1
    return diff

for line1 in lines:
    for line2 in lines:
        if checkdiff(line1, line2) == 1:
            print(line1)
            print(line2)
