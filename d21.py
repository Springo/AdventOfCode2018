def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d21input.txt")

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

ins = []
for line in lines[1:]:
    l1 = line.split(" ")
    ins.append([l1[0], int(l1[1]), int(l1[2]), int(l1[3])])

for a in range(1):
    regs = [0] * 6
    regs[0] = 0
    done = False
    found = dict()
    while not done:
    #for i in range(2000):
        cur = ins[regs[2]]
        if regs[2] == 30:
            print(regs[1])
            print(regs[4])
            if (regs[1], regs[4]) not in found:
                found[(regs[1], regs[4])] = 1
            else:
                print("HALTED")
                exit()
        #print("{}: {} - {}".format(regs[2], cur, regs))
        eval(cur[0])(regs, cur[1], cur[2], cur[3])
        if regs[2] >= len(ins) or regs[2] < 0:
            #print(i + 1)
            done = True
        regs[2] += 1

    if done:
        print("Success!")
        print(regs)


regs = [0] * 6
regs[0] = 0

"""
#regs[1] = 123
#regs[1] = regs[1] & 456
#regs[1] = (regs[1] == 72)
regs[1] = 1

#addr 1 2 2
regs[2] = regs[1] + regs[2]

#seti 0 0 2
regs[2] = 0

#seti 0 9 1
regs[1] = 0
"""


