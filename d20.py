import sys
from random import randint

sys.setrecursionlimit(10000)

def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d20input.txt")
#lines = readFile("test.txt")
reg_inp = lines[0][1:-1]

class Cell:
    def __init__(self, id):
        self.up = 0
        self.right = 0
        self.down = 0
        self.left = 0
        self.id = id

    def __repr__(self):
        out = "\n"
        if self.up == 0:
            out += "###\n"
        else:
            out += "#O#\n"
        if self.left == 0:
            out += "#"
        else:
            out += "O"
        out += "_"
        if self.right == 0:
            out += "#"
        else:
            out += "O"
        out += "\n"
        if self.down == 0:
            out += "###"
        else:
            out += "#O#"
        out += "\n"
        return out

cur_id = 1
start = Cell(0)
cur_loc = start

def parseReg(reg, cur_loc, marks):
    global cur_id
    if len(reg) < 1:
        return
    ends = []
    if ')' in reg:
        cutoff = reg.find(')')
    else:
        cutoff = len(reg)
    cur_reg = reg[:cutoff]
    for c in cur_reg:
        if c == '(':
            marks.append(cur_loc)
        elif c == '|':
            ends.append(cur_loc)
            cur_loc = marks[-1]
        #elif c == ')':
        #    marks.pop()
        elif c == 'N':
            if cur_loc.up == 0:
                new_cell = Cell(cur_id)
                cur_id += 1
                cur_loc.up = new_cell
                new_cell.down = cur_loc
                cur_loc = new_cell
            else:
                cur_loc = cur_loc.up
        elif c == 'E':
            if cur_loc.right == 0:
                new_cell = Cell(cur_id)
                cur_id += 1
                cur_loc.right = new_cell
                new_cell.left = cur_loc
                cur_loc = new_cell
            else:
                cur_loc = cur_loc.right
        elif c == 'S':
            if cur_loc.down == 0:
                new_cell = Cell(cur_id)
                cur_id += 1
                cur_loc.down = new_cell
                new_cell.up = cur_loc
                cur_loc = new_cell
            else:
                cur_loc = cur_loc.down
        elif c == 'W':
            if cur_loc.left == 0:
                new_cell = Cell(cur_id)
                cur_id += 1
                cur_loc.left = new_cell
                new_cell.right = cur_loc
                cur_loc = new_cell
            else:
                cur_loc = cur_loc.left
    marks.pop()
    ends.append(cur_loc)
    later_reg = reg[cutoff + 1:]
    #for loc in ends:
    #    parseReg(later_reg, loc, marks[:])
    loc = ends[randint(0, len(ends) - 1)]
    parseReg(later_reg, loc, marks[:])

for i in range(10000):
    cur_loc = start
    parseReg(reg_inp, cur_loc, [cur_loc])

Q = [[start, 0]]
biggest = 0
found = dict()
found[0] = 1
while len(Q) > 0:
    cur = Q.pop(0)
    cur_loc = cur[0]
    u = cur_loc.up
    r = cur_loc.right
    d = cur_loc.down
    l = cur_loc.left
    if u != 0 and u.id not in found:
        found[u.id] = 1
        Q.append([u, cur[1] + 1])
        if cur[1] + 1 > biggest:
            biggest = cur[1] + 1
    if r != 0 and r.id not in found:
        found[r.id] = 1
        Q.append([r, cur[1] + 1])
        if cur[1] + 1 > biggest:
            biggest = cur[1] + 1
    if d != 0 and d.id not in found:
        found[d.id] = 1
        Q.append([d, cur[1] + 1])
        if cur[1] + 1 > biggest:
            biggest = cur[1] + 1
    if l != 0 and l.id not in found:
        found[l.id] = 1
        Q.append([l, cur[1] + 1])
        if cur[1] + 1 > biggest:
            biggest = cur[1] + 1

print(biggest)
# ENWWWSSEEE
# ENNWSWWSSSEENEENNN
