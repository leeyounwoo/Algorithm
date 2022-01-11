from collections import deque
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    case = deque(map(int, input().split()))

    for _ in range(m):
        case.append(case.popleft())

    print('#{} {}'.format(tc+1, case[0]))