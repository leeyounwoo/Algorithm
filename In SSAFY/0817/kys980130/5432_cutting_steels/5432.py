import sys
sys.stdin = open("input.txt")
N = int(input())
for tc in range(1, N+1):
    arr = list(input())
    l = len(arr)
    i = 0
    total = 0
    stick = 0
    while i < l:
        if arr[i] == '(' and arr[i+1] == ')':
            total += stick
            i += 2
        elif arr[i] == '(':
            stick += 1
            i += 1
        else:
            total += 1
            stick -= 1
            i += 1
    print('#{} {}'.format(tc, total))
