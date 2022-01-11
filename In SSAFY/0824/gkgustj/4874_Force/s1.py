import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    string = input().split()
    stack = []

    try:
        for s in string:
            if s.isnumeric():
                stack.append(int(s))
            elif s == '+':
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 + num2)
            elif s == '-':
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 - num2)
            elif s == '*':
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 * num2)
            elif s == '/':
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 // num2)
            else:
                result = stack.pop()
        if stack:
            result = 'error'
    except:
        result = 'error'

    print('#{} {}'.format(t, result))