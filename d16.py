import ast

def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d16input.txt")
lines1 = lines[:3104]
lines2 = lines[3106:]

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

samples = []
for i in range(0, len(lines1), 4):
    l1 = lines1[i][9:-1].split(", ")
    bef = [int(c) for c in l1]
    l2 = lines1[i + 1].split(" ")
    ins = [int(c) for c in l2]
    l3 = lines1[i + 2][9:-1].split(", ")
    aft = [int(c) for c in l3]
    samples.append([bef, ins, aft])

threeop = 0
for s in samples:
    bef = s[0]
    ins = s[1]
    aft = s[2]

    results = []
    results.append(addr(bef[:], ins[1], ins[2], ins[3]))
    results.append(addi(bef[:], ins[1], ins[2], ins[3]))
    results.append(mulr(bef[:], ins[1], ins[2], ins[3]))
    results.append(muli(bef[:], ins[1], ins[2], ins[3]))
    results.append(banr(bef[:], ins[1], ins[2], ins[3]))
    results.append(bani(bef[:], ins[1], ins[2], ins[3]))
    results.append(borr(bef[:], ins[1], ins[2], ins[3]))
    results.append(bori(bef[:], ins[1], ins[2], ins[3]))
    results.append(setr(bef[:], ins[1], ins[2], ins[3]))
    results.append(seti(bef[:], ins[1], ins[2], ins[3]))
    results.append(gtir(bef[:], ins[1], ins[2], ins[3]))
    results.append(gtri(bef[:], ins[1], ins[2], ins[3]))
    results.append(gtrr(bef[:], ins[1], ins[2], ins[3]))
    results.append(eqir(bef[:], ins[1], ins[2], ins[3]))
    results.append(eqri(bef[:], ins[1], ins[2], ins[3]))
    results.append(eqrr(bef[:], ins[1], ins[2], ins[3]))

    corr_count = 0
    i = 0
    for r in results:
        if r == aft:
            corr_count += 1
    #        if ins[0] == 0:
    #            print(i)
        i += 1

    if corr_count >= 3:
        threeop += 1

    #if corr_count == 1:
    #    print(s)

print(threeop)

ins_list = []
for line in lines2:
    l1 = line.split(" ")
    ins_list.append([int(c) for c in l1])

# 0 - borr
# 1 - seti
# 2 - mulr
# 3 - eqri
# 4 - banr
# 5 - bori
# 6 - bani
# 7 - gtri
# 8 - addr
# 9 - muli
# 10 - addi
# 11 - eqrr
# 12 - gtir
# 13 - eqir
# 14 - setr
# 15 - gtrr

regs = [0,0,0,0]
for ins in ins_list:
    if ins[0] == 0:
        borr(regs, ins[1], ins[2], ins[3])
    elif ins[0] == 1:
        seti(regs, ins[1], ins[2], ins[3])
    elif ins[0] == 2:
        mulr(regs, ins[1], ins[2], ins[3])
    elif ins[0] == 3:
        eqri(regs, ins[1], ins[2], ins[3])
    elif ins[0] == 4:
        banr(regs, ins[1], ins[2], ins[3])
    elif ins[0] == 5:
        bori(regs, ins[1], ins[2], ins[3])
    elif ins[0] == 6:
        bani(regs, ins[1], ins[2], ins[3])
    elif ins[0] == 7:
        gtri(regs, ins[1], ins[2], ins[3])
    elif ins[0] == 8:
        addr(regs, ins[1], ins[2], ins[3])
    elif ins[0] == 9:
        muli(regs, ins[1], ins[2], ins[3])
    elif ins[0] == 10:
        addi(regs, ins[1], ins[2], ins[3])
    elif ins[0] == 11:
        eqrr(regs, ins[1], ins[2], ins[3])
    elif ins[0] == 12:
        gtir(regs, ins[1], ins[2], ins[3])
    elif ins[0] == 13:
        eqir(regs, ins[1], ins[2], ins[3])
    elif ins[0] == 14:
        setr(regs, ins[1], ins[2], ins[3])
    elif ins[0] == 15:
        gtrr(regs, ins[1], ins[2], ins[3])
print(regs[0])
