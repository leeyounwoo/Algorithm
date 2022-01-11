import sys
sys.stdin = open('input.txt')

def brackets_check(s):
    stack = []
    for i in s:
        if i in ['(', '{']:
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] != '(':
                return 0
            else:
                stack.pop()
        elif i == '}':
            if not stack or stack[-1] != '{':
                return 0
            else:
                stack.pop()
    if stack:
        return 0
    return 1

T = int(input())
for tc in range(T):
    s = input()
    print('#{0} {1}'.format(tc+1, brackets_check(s)))





