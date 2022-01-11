import sys
sys.stdin = open('input.txt')
from collections import deque

for tc in range(1, t+1):
    t = int(input())
    n = deque(list(map(int, input().split())))
    # 10 6 12 8 9 4 1 3
    # 3 9 4 9 4 4 3 0

    idx = 0
    while n[-1] > 0: # 마지막 숫자가 0 이상일때까지
        idx += 1
        if idx == 6:
            idx = 1
        popped = n.popleft()
        popped -= idx
        n.append(popped)
    n[-1] = 0

    print('#{}'.format(tc), end="")
    print(*n)