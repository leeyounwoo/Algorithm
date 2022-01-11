def push(item):
    stack.append(item)

def pop():
    if stack:
        return stack.pop()
    else:
        print('stack is empty!')
        return

stack = []

push(1)
push(2)
push(3)

print(pop())
print(pop())
print(pop())
print(pop())