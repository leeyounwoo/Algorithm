import sys
import math

def binarySearch(start, end, find):
    global ans
    if start > end:
        return
    mid = (start + end) // 2
    cnt = 0
    for i in range(len(lines)):
        cnt += lines[i] // mid
    if cnt >= find:
        ans = mid
        binarySearch(mid+1, end, find)
    else:
        binarySearch(start, mid-1, find)


sys.stdin = open('input.txt')
k, n = map(int, sys.stdin.readline().split())
lines = []
for i in range(k):
    lines.append(int(sys.stdin.readline()))
lines.sort()
ans = 1
binarySearch(1, lines[-1], n)
print(ans)