import sys
sys.stdin = open('input.txt')

from collections import deque
for T in range(1, 1+int(input())):
    N, M = map(int, input().split())
    queue = deque(list(map(int, input().split())))

    for _ in range(M):
        temp = queue.popleft()
        queue.append(temp)
    print('#{} {}'.format(T, *queue))
    # print(*queue)