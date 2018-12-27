def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines

class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, head):
        self.head = head

np = 427
lm = 7072300

cur = Node(0)
ll = LinkedList(cur)
cur.next = Node(1)
cur.prev = cur.next
cur.next.prev = cur
cur.prev.next = cur
cur = cur.next

lastind = 1
turn = 1
scores = dict()
counter = 2
for i in range(2, lm+1):
    if i % 23 == 0:
        if turn not in scores:
            scores[turn] = 0
        scores[turn] += i
        for j in range(7):
            cur = cur.prev
        scores[turn] += cur.data
        cur = cur.next
        b = cur.prev.prev
        b.next = cur
        cur.prev = b
        turn = (turn + 1) % np
        counter -= 1
    else:
        cur = cur.next
        newnode = Node(i)
        f = cur.next
        cur.next = newnode
        newnode.prev = cur
        newnode.next = f
        f.prev = newnode
        cur = cur.next
        turn = (turn + 1) % np
        counter += 1

best_score = max(scores, key=scores.get)
print(scores[best_score])
