def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        print('스택이 비어있습니다!')
        return
    return stack.pop()

stack = []

push(1) # stack: [1]
push(2) # stack: [1, 2]
push(3) # stack: [1, 2, 3]

print(pop())