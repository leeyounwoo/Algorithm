import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    for _ in range(M):
        queue.append(queue.pop(0))

    print('#{} {}'.format(t, queue.pop(0)))