import sys
sys.stdin = open('input.txt')

from collections import deque


def cal(num, j):
    if j == '+1':
        return num + 1
    elif j == '-1':
        return num - 1
    elif j == '*2':
        return num * 2
    elif j == '-10':
        return num - 10


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    case = ['+1', '-1', '*2', '-10']

    flag = 0
    result = 0
    queue = deque()
    queue.append([N, 0])

    while queue:
        if flag:
            break
        v, cnt = queue.popleft()

        for i in case:
            number = cal(v, i)
            if number == M:
                result = cnt + 1
                flag = 1
                break
            else:
                queue.append([number, cnt+1])
    print('#{} {}'.format(tc+1, result))
