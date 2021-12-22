import sys
from collections import deque

sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
ans = deque()
numbers = deque()
check = [False for _ in range(n)]
flag = 1
for i in range(n):
    temp = int(sys.stdin.readline())
    # print(numbers, temp)
    if temp not in numbers:
        for j in range(flag, temp+1):
            numbers.append(j)
            ans.append('+')
            flag = j+1
        numbers.pop()
        ans.append('-')
    elif numbers[-1] == temp:
        numbers.pop()
        ans.append('-')
    else:
        ans = 'NO'
        break
if ans == 'NO':
    print(ans)
else:
    for i in range(len(ans)):
        print(ans[i])

