def push(item):
    stack.append(item)  # return이 없어도 None이 반환되는 거


def pop():  # 맨 뒤에 있는 것만 빼
    if len(stack) == 0:
        print('스택이 비어있습니다!')
        return
    return stack.pop()


stack = []

push(1)  # stack: [1]
push(2)  # stack: [1, 2]
push(3)  # stack: [1, 2, 3]

print(pop())  # 3
print(pop())  # 2
print(pop())  # 1
print(stack)  # []
