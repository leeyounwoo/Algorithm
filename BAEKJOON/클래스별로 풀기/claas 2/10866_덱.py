import sys
from collections import deque

sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
deq = deque()
for i in range(n):
    command = str(sys.stdin.readline())
    if command[:2] == 'pu':
        if command[5] == 'f':
            deq.appendleft(int(list(command.split())[1]))
        else:
            deq.append(int(list(command.split())[1]))
    if command[:2] == 'po':
        if command[4] == 'f':
            if deq:
                print(deq.popleft())
            else:
                print(-1)
        else:
            if deq:
                print(deq.pop())
            else:
                print(-1)
    if command[:2] == 'si':
        print(len(deq))
    if command[:2] == 'em':
        if deq:
            print(0)
        else:
            print(1)
    if command[:2] == 'fr':
        if deq:
            print(deq[0])
        else:
            print(-1)
    if command[:2] == 'ba':
        if deq:
            print(deq[-1])
        else:
            print(-1)


