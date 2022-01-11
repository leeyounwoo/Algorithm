import sys

sys.stdin = open('input.txt')
for T in range(1, 11):
    N, number = map(int, input().split())
    stack = []
    for i in range(N):
        number, r = divmod(number, 10)
        if not len(stack) or r != stack[-1]:
            stack.append(r)
        else:
            stack.pop()

    ans = 0
    mul = 1
    for i in range(len(stack)):
        ans += (mul * stack[i])
        mul *= 10
    print('#{} {}'.format(T, ans))