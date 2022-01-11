import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(TC):
    string = list(input().split())
    stack = []
    token = ['+', '-', '*', '/']
    answer = "error"

    for s in string:
        if s in token:
            if len(stack) < 2:
                break
            a = stack.pop()
            b = stack.pop()
            if s == '+':
                stack.append(b + a)
            elif s == '-':
                stack.append(b - a)
            elif s == '*':
                stack.append(b * a)
            elif s == '/':
                stack.append(b // a)
        elif s == '.' and len(stack) == 1:
            answer = stack.pop()
        elif s.isdigit():
            stack.append(int(s))
        else:
            break

    print("#{} {}".format(tc+1, answer))