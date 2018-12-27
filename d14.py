inp = 330121
str_inp = str(inp)

class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, head1, head2, tail):
        self.tail = tail
        self.head1 = head1
        self.head2 = head2

n1 = Node(3)
n2 = Node(7)
n1.next = n2
n1.prev = n2
n2.next = n1
n2.prev = n1
r = LinkedList(n1, n2, n2)
stacker = []

total = 2
marker = 0
#while total < inp + 10:
i = 1
while len(stacker) < len(str_inp):
    newrec = str(r.head1.data + r.head2.data)
    for c in newrec:
        i += 1
        if i % 100000 == 0:
            print(i)
        newn = Node(int(c))
        newn.prev = r.tail
        newn.next = r.tail.next
        r.tail.next.prev = newn
        r.tail.next = newn
        r.tail = r.tail.next
        total += 1
        if str_inp[len(stacker)] == c:
            stacker.append(i)
            if len(stacker) == len(str_inp):
                break
        else:
            stacker = []
        #if total == inp:
        #    marker = r.tail
    for j in range(r.head1.data + 1):
        r.head1 = r.head1.next
    for j in range(r.head2.data + 1):
        r.head2 = r.head2.next

#for i in range(10):
#    marker = marker.prev
#    print(marker.data, end='')

print(stacker[0])
