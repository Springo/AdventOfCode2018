def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d12input.txt")
state = lines[0].split(":")[1][1:]
for i in range(25):
    state = '.' + state + '.'
for i in range(300):
    state = state + '.'
s_list = [c for c in state]

rules = dict()
for line in lines[2:]:
    l1 = line.split(" => ")
    rules[l1[0]] = l1[1]

potcenter = 25
for gen in range(200):
    new_s = s_list[:]
    for i in range(2, len(s_list) - 2):
        key = ''.join(s_list[i - 2: i + 3])
        if key in rules:
            result = rules[key]
            new_s[i] = result
    s_list = new_s

    total = 0
    for i in range(len(s_list)):
        if s_list[i] == "#":
            total += i - potcenter
    print(total)
    print(gen)
    print(''.join(s_list))

print(4108 + 20 * (50 * (10 ** 9) - 180))
