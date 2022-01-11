from collections import deque
import sys
sys.stdin = open('input.txt')

def find_M(N):
    global numbers

    queue = deque()
    queue.append((N, 0))

    numbers[N] = 1

    while queue:
        number, cnt = queue.popleft()

        if number == M:
            return cnt
        
        if number+1 <= 1000000 and not numbers[number+1]:
            numbers[number+1] = 1
            queue.append((number+1, cnt+1))

        if number-1 > 0 and not numbers[number-1]:
            numbers[number-1] = 1
            queue.append((number-1, cnt+1))

        if number*2 <= 1000000 and not numbers[number*2]:
            numbers[number*2] = 1
            queue.append((number*2, cnt+1))

        if number-10 > 0 and not numbers[number-10]:
            numbers[number-10] = 1
            queue.append((number-10, cnt+1))


T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    numbers = [0 for _ in range(1000001)]

    print('#{} {}'.format(t, find_M(N)))