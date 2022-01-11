from collections import deque
import sys
sys.stdin = open('input.txt')

def my_calc(num, calc):
    if calc == 0:
        return num + 1
    elif calc == 1:
        return num - 1
    elif calc == 2:
        return num * 2
    elif calc == 3:
        return num - 10


def bfs(N, M):
    global tc
    Q = deque()
    Q.append((N, 0))
    while Q:
        num, cnt = Q.popleft()
        for i in range(4):
            # 계산 실행
            next_num = my_calc(num, i)
            # 일치한다면 카운트 계산
            if next_num == M:
                return cnt + 1
            # 일치하지 않는다면 조건을 확인하며 계산 반복
            elif 1 <= next_num <= 1000000:
                Q.append((next_num, cnt + 1))



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    num_lst = [0] * 1000001  # M < 1000000
    print('#{} {}'.format(tc, bfs(N, M)))