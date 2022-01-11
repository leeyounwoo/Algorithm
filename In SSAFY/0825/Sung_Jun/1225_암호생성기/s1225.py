import sys
sys.stdin = open('input.txt')

t = 10
for _ in range(t):
    tc = int(input())
    numbers = list(map(int, input().split()))

    i = -1
    while True:
        i = i + 1
        w = (i % 5) + 1
        v = numbers.pop(0) - w
        if v > 0:
            numbers.append(v)
        else:
            numbers.append(0)
            break

    print('#{}'.format(tc), end=' ')
    print(*numbers)
