import sys
sys.stdin = open("input.txt")

def is_empty():
    # 만약 스택이 있으면 F 없으면 T
    if stack:
        return False
    return True

def check(arr):
    for i in arr:
        if i == '(' or i == '{':
            stack.append(i)

        elif i == ')':
            if len(stack) == 0:
                return 0

            elif stack[-1] == '(':
                stack.pop()
            else:
                return 0

        elif i == '}':
            if len(stack) == 0:
                return 0

            elif stack[-1] == '{':
                stack.pop()

            else:
                return 0

    if is_empty():
        return 1
    return 0

T = int(input())
for tc in range(T):
    stack = []
    arr = input()
    print('#{} {}'.format(tc+1, check(arr)))
