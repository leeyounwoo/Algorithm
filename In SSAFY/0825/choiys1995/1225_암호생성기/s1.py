import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = input()
    queue = list(map(int, input().split()))

    i = 0
    while True:
        t = queue.pop(0) - (i % 5 + 1)
        if t <= 0:
            queue.append(0)
            break
        queue.append(t)
        i += 1

    print('#{}'.format(tc), *queue)