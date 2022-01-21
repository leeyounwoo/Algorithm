import sys


def input():
    return sys.stdin.readline().rstrip()

def bfs(start, goal, cnt):
    global ans
    # print(start)
    if start == goal:
        if ans == -1 or ans > cnt:
            ans = cnt
        return
    num1 = start * 2
    num2 = int(str(start) + '1')
    if num1 <= goal and (ans == -1 or cnt+1 < ans):
        bfs(num1, goal, cnt+1)
    if num2 <= goal and (ans == -1 or cnt+1 < ans):
        bfs(num2, goal, cnt+1)



sys.stdin = open('input.txt')
n, m = map(int, input().split())
ans = -1
bfs(n, m, 1)
print(ans)