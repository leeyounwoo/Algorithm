import sys
sys.stdin = open('input.txt')
from collections import deque

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    s = deque(list(map(str, input().split())))
    temp1 = deque([])
    temp2 = deque([])
    flag = True
    if len(s) % 2: # 홀수 갯수라면
        m = (len(s) // 2) + 1
    else:
        m = len(s) // 2

    count = 0
    while s:
        if count < m:
            temp1.append(s.popleft())
        else:
            temp2.append(s.popleft())
        count += 1

    result = []

    flag = True
    while temp1 or temp2:
        if flag:
            result.append(temp1.popleft())
            flag = False
        elif not flag:
            result.append(temp2.popleft())
            flag = True
        # print(result)
    print('#{} {}'.format(tc, ' '.join(result)))