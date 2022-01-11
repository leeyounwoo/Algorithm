class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


front, rear = None, None


def enQ(item):  # 연결큐에 삽입하는 연산
    global  front, rear

    new_node = Node(item)  # 새로운 노드 생성

    if front == None:  # 큐가 비어있다면
        front = new_node

    else:
        rear.next = new_node
    rear = new_node


def printQ():
    f = front
    result = ''

    while f:
        result += f.item
        f = f.next

    return result


def deQ():
    global front, rear

    if front == None:
        print('큐가 비어있습니다.')
        return None

    item = front.item
    front = front.next

    # 만약 꺼냈을 때 큐가 비어있게 된다면...
    if front == None:
        rear = None

    return item


enQ('A')
enQ('B')
enQ('C')
print(printQ())
print(deQ())  # A
print(deQ())  # B
print(deQ())  # C
print(deQ())  # 에러 메세지(None)