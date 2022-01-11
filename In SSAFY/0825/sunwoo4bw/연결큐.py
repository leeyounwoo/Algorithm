class Node :
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

front, rear = None, None

def enQ(item) : # 연결큐에 삽입하는 연산
    global front, rear

    new_node = Node(item)  # 새로운 노드 생성

    if front == None : # 첫 번째가 비어있다면 = 큐가 비어있다면
        front = new_node
    else :
        rear.next = new_node  # rear.next에 지금 들어올 new_node를
    rear = new_node

def printQ():
    f = front
    result = ''

    while f: # f가 none이 아닌 동안
        result += f.item  # 현재 아이템 넣어줘
        f = f.next # f의 다음 꺼롤 f로 갱신시켜줘
    return result

def deQ():
    global front, rear   # 선입선출 - 먼저 들어온 게 먼저 나가

    if front == None :
        print('큐가 비어있습니다.')
        return None   # 마지막 print(deQ())가 에러 메세지 (None) 뜨는 이유

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
print(deQ()) # A
print(deQ()) # B
print(deQ()) # C
print(deQ()) # 에러 메세지 (None)