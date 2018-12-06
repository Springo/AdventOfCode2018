def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d01input.txt")
tot = 0
freq = dict()
freq[0] = 1
while True:
    for line in lines:
        tot += int(line)
        if tot in freq:
            print(tot)
            exit()
        else:
            freq[tot] = 1
