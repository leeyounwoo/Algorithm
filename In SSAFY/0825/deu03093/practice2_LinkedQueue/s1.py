class Node:
    def __init__(self, item, next_node=None):
        self.item = item
        self.next_node = next_node

front, rear = None, None

def enQueue(item):
    global front, rear
    new_node = Node(item)
    if front == None:
        front = new_node
    else:
        rear.next_node = new_node
    rear = new_node

def printQ():
    f = front
    result = ''

    while f:
        result += f.item
        f = f.next_node

    return result

def deQueue():
    global front, rear

    if front == None:
        print('큐가 비어있습니다')
        return None

    item = front.item
    front = front.next_node

    if front == None:
        rear = None

    return item


enQueue('A')
enQueue('B')
enQueue('C')
print(printQ())
print(deQueue())
print(deQueue())
print(deQueue())
print(deQueue())
print(printQ())