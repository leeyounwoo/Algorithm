import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    string = list(input().split())
    stack = []

    result = 'error'
    for char in string:
        if char in '+-*/.':
            if char == '.':
                if len(stack) == 1:
                    result = stack.pop()
                break
            elif len(stack) < 2:
                break

            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a // b)
        else:
            stack.append(int(char))

    print('#{} {}'.format(tc, result))