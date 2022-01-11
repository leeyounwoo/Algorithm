import sys

sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    sticks = input()

    result = True
    stack = []
    for i in sticks:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                result = False
            stack.pop()

    if len(stack) > 0:
        result = False

    print(result)
