import sys
sys.stdin = open('input.txt')
from collections import deque

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    number = deque(list(map(int, input().split())))

    for _ in range(m):
        number.append(number.popleft())

    answer = number[0]
    print('#{} {}'.format(tc, answer))