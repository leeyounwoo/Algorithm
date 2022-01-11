class Node:
    def __init__(self, item, next = None):
        self.item = item
        self.next = next

front, rear = None, None

def enq(item):
    global front, rear

    new_node = Node(item)
    if front == None:
        front = new_node
    else:
        rear.next = new_node
    rear = new_node

def deq():
    global front, rear

    if front == None:
        print("비어있는 큐")
        return None
    item = front.item
    front = front.next

    if front == None:
        rear = None
    return item

def printQ():
    f = front
    while f:
        print(f.item, end = " ")
        f = f.next
    print()

enq('a')
enq('b')
enq('c')
printQ()
print(deq())
print(deq())
print(deq())