import sys
sys.stdin = open('input.txt')

for _ in range(2):
    bracket = input()
    stack = []
    for i in bracket:
        if i == '(':
            stack.append(')')
        elif i == ')':
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
                break
    if stack:
        print('No')
    else:
        print('Yes')