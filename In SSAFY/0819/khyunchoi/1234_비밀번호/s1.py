import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N, password = input().split()
    N = int(N)
    stack = []

    for num in password:
        if len(stack) == 0:
            stack.append(num)
            continue

        if num == stack[-1]:
            stack.pop()
        else:
            stack.append(num)

    print('#{} '.format(tc), end='')
    for num in stack:
        print(num, end='')
    print()