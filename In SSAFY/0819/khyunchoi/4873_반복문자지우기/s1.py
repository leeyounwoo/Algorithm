import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    text = input()
    stack = []

    for i in range(len(text)):
        stack.append(text[i])
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()

    result = len(stack)
    print('#{} {}'.format(tc, result))