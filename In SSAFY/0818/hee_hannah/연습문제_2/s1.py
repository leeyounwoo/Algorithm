import sys
sys.stdin = open('input.txt')

def push(item):
    stack.append(item)



t = int(input())


for _ in range(t):
    a = input()
    stack = []
    for i in a:
        if i == '(':
            push(i)
        elif i == ')':
            stack.pop()
    if len(stack) == 0:
        print('ok')
    else:
        print('wrong')


