import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


# 동기화 메소드
def sync(q):
    while q and not check[q[0][1]]:
        heapq.heappop(q)

for _ in range(int(input())):
    n = int(input())
    max_q, min_q = [], []
    check = [False] * 1_000_001  # 동기화 아이디

    for i in range(n):
        command, num = input().split()

        if command == 'I':
            heapq.heappush(min_q, (int(num), i))
            heapq.heappush(max_q, (-int(num), i))
            check[i] = True
        elif num == '1':
            sync(max_q)

            if max_q:
                check[max_q[0][1]] = False
                heapq.heappop(max_q)
        else:
            sync(min_q)

            if min_q:
                check[min_q[0][1]] = False
                heapq.heappop(min_q)

    sync(min_q)
    sync(max_q)
    if max_q:
        print(-max_q[0][0], min_q[0][0])
    else:
        print('EMPTY')
