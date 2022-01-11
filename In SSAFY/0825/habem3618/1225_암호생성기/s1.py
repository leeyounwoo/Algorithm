from collections import deque
import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    t = int(input())
    pwd = deque(list(map(int, input().split())))

    count = 1
    while True:

        pwd_x = pwd.popleft()
        if pwd_x - count <= 0:
            pwd.append(0)
            break

        else:
            pwd.append(pwd_x - count)
        count += 1

        if count > 5:
            count = 1

    print('#{}'.format(tc), *pwd)

