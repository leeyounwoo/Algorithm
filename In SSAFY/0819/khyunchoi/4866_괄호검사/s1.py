import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    text = input()
    stack = []

    result = 1
    for i in range(len(text)):
        if text[i] == '(' or text[i] == '{':
            stack.append(text[i])
        elif text[i] == ')' or text[i] == '}':
            if len(stack) == 0:
                result = 0
                break

            if text[i] == ')' and stack.pop() != '(':
                result = 0
                break
            elif text[i] == '}' and stack.pop() != '{':
                result = 0
                break

    if stack:
        result = 0

    print('#{} {}'.format(tc, result))