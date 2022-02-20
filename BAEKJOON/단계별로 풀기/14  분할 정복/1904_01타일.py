import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
n = int(input())
d = deque([0, 1, 2])

if n <= 2:
    print(d[n])
else:
    for i in range(3, n+1):
        d.popleft()
        temp = (d[0] + d[1]) % 15746
        d.append(temp)
    print(d[-1])