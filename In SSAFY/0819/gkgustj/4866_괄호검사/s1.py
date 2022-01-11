import sys

sys.stdin = open('input.txt')

def check(string):
    stack = []

    for s in string:
        if s == '(' or s == '{':
            stack.append(s)

        elif s == ')':
            if not stack:
                return 0
            if stack.pop() != '(':
                return 0

        elif s == '}':
            if not stack:
                return 0
            if stack.pop() != '{':
                return 0

    if stack:
        return 0
    return 1


T = int(input())

for t in range(1, T+1):
    string = input()
    print('#{} {}'.format(t, check(string)))