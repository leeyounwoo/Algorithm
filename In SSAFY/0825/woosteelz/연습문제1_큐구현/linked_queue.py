class Node:
    def __init__(self, data, next=None):
        self.next = next
        self.data = data

front, tail = None, None

def enqueue(data):
    global front, tail
    new_node = Node(data)

    if not front:
        front = new_node
    else:
        tail.next = new_node
    tail = new_node

def dequeue():
    global front, tail

    if not front:
        print('Queue is empty!')
        return None
    data = front.data
    front = front.next
    return data

def print_queue():
    global front, tail
    curr = front
    while curr:
        print(curr.data)
        curr = curr.next

enqueue('A')
enqueue('B')
enqueue('C')

print_queue()

dequeue()

print_queue()