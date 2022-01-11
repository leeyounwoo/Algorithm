import sys
from collections import deque

sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    password = deque(map(int, input().split()))

    i = 1
    while True:
        temp = password.popleft() - i
        if temp <= 0:
            password.append(0)
            break
        else:
            password.append(temp)
        i += 1
        if i > 5:
            i = 1


    print('#{}'.format(tc), *password)