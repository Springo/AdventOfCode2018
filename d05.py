def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

lines = readFile("d05input.txt")
inp = lines[0]

def react(inp):
    stack = []
    for i in range(len(inp)):
        if len(stack) > 0 and (stack[-1] != inp[i] and (stack[-1].lower() == inp[i].lower())):
            stack.pop()
        else:
            stack.append(inp[i])
    return len(stack)

def remlet(let, inp):
    lets = ""
    for i in range(len(inp)):
        if inp[i].lower() != let.lower():
            lets = lets + inp[i]
    return lets


"""
cont = True
prev = inp
while cont:
    cont = False
    for i in range(len(inp) - 1):
        if inp[i] != inp[i + 1] and (inp[i].lower() == inp[i+1].lower()):
            newinp = inp[:i] + inp[i + 2:]
            prev = inp
            inp = newinp
            cont = True
            print(len(inp))
            break;
"""
print(react(inp))

let_count = dict()
for c in inp:
    if c.lower() not in let_count:
        let_count[c.lower()] = 1

smallest = len(inp)
for key in let_count:
    newinp = remlet(key, inp)
    res = react(newinp)
    if res < smallest:
        smallest = res
print(smallest)
