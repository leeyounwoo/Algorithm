def push(item):
    # global stack 이거 매개변수(리스트) 지정 안해줘도됨 그치만 max_size같은 상수는 해줘야함
    stack.append(item) #리턴이 없으면 none 반환됨 꼭 return써야하는건 아님..

def pop():
    if len(stack) == 0:
        print('스택이 비어있습니다')
        return
    return stack.pop()


max_size = 100
stack = []
push(1) # stack: [1]
push(2) # stack: [1,2]
push(3) # stack: [1,2,3]

print(pop()) # 3
print(pop()) # 2
print(pop()) # 1
print(pop())
print(stack) # []
