import sys
sys.stdin = open("input.txt")

def check(arr):
    stack = []
    for i in arr:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return len(stack)

T = int(input())
for tc in range(T):
    arr = input()
    print('#{} {}'.format(tc + 1, check(arr)))