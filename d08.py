def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d08input.txt")
inp = [int(x) for x in lines[0].split(' ')]

metadict = dict()
childdict = dict()

def getMetaData(orig_root):
    root = orig_root
    childcount = inp[root]
    metacount = inp[root + 1]
    if childcount > 0:
        childdict[root] = []
    root = root + 2
    for i in range(childcount):
        childdict[orig_root].append(root)
        newroot, _ = getMetaData(root)
        root = newroot
    metadata = []
    for i in range(metacount):
        metadata.append(inp[root + i])
    root += metacount
    metadict[orig_root] = metadata
    return root, metadata

print(getMetaData(0))
total = 0
for key in metadict:
    total += sum(metadict[key])

print(total)

def getValue(orig_root):
    if orig_root not in metadict:
        print(orig_root)
        return 0
    if orig_root not in childdict:
        return sum(metadict[orig_root])
    total = 0
    for m in metadict[orig_root]:
        if m <= len(childdict[orig_root]):
            total += getValue(childdict[orig_root][m - 1])
    return total

print(getValue(0))
