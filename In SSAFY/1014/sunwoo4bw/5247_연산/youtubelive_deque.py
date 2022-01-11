import sys
sys.stdin = open('input.txt')

from collections import deque
# Boolean, 큐 사이즈로 묶어서

def BFS2():
    Q = deque()
    Q.append(N)
    memo[N] = True

    ans = 0

    while Q :
        size = len(Q)
        for i in range(size):
            num = Q.popleft()
            if num == M :
                return ans
            for j in (num+1, num-1, num*2, num-10):
                if 0 < j <= 1000000 and not memo[j]:
                    memo[j] = True
                    Q.append(j)
        ans += 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N1=M, N,M 100만 이하의 자연수이다.

    memo = [False] * 1000001
    print('#{} {}'.format(tc, BFS2()))