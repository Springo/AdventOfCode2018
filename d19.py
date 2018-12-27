def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

def addr(reg, a, b, c):
    reg[c] = reg[a] + reg[b]
    return reg

def addi(reg, a, b, c):
    reg[c] = reg[a] + b
    return reg

def mulr(reg, a, b, c):
    reg[c] = reg[a] * reg[b]
    return reg

def muli(reg, a, b, c):
    reg[c] = reg[a] * b
    return reg

def banr(reg, a, b, c):
    reg[c] = reg[a] & reg[b]
    return reg

def bani(reg, a, b, c):
    reg[c] = reg[a] & b
    return reg

def borr(reg, a, b, c):
    reg[c] = reg[a] | reg[b]
    return reg

def bori(reg, a, b, c):
    reg[c] = reg[a] | b
    return reg

def setr(reg, a, b, c):
    reg[c] = reg[a]
    return reg

def seti(reg, a, b, c):
    reg[c] = a
    return reg

def gtir(reg, a, b, c):
    if a > reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg

def gtri(reg, a, b, c):
    if reg[a] > b:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg

def gtrr(reg, a, b, c):
    if reg[a] > reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg

def eqir(reg, a, b, c):
    if a == reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg

def eqri(reg, a, b, c):
    if reg[a] == b:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg

def eqrr(reg, a, b, c):
    if reg[a] == reg[b]:
        reg[c] = 1
    else:
        reg[c] = 0
    return reg

lines = readFile("d19input.txt")
ins = []
for line in lines[1:]:
    l1 = line.split(" ")
    ins.append([l1[0], int(l1[1]), int(l1[2]), int(l1[3])])
    print()

regs = [0] * 6
#regs[0] = 1
#regs = [1, 2, 5275638, 0, 3, 10551276]
#regs = [3, 2, 10551276, 0, 3, 10551276]
#regs = [3, 3, 3517092, 0, 3, 10551276]
#regs = [1, 2, 4000000, 0, 3, 10551276]

done = False
#while not done:
for i in range(1):
    cur = ins[regs[4]]
    print("{}: {} - {}".format(regs[4], cur, regs))
    eval(cur[0])(regs, cur[1], cur[2], cur[3])
    if regs[4] >= len(ins) or regs[4] < 0:
        done = True
    regs[4] += 1

print(regs)
print(regs[0])

total = 0
for i in range(1, 10551277):
    if 10551276 % i == 0:
        total += i
print(total)
