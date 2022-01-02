import sys
import heapq
sys.stdin = open('input.txt')
n = int(input())
heap = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    # print('num', num)
    if num == 0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))

    else:
        heapq.heappush(heap, -num)
