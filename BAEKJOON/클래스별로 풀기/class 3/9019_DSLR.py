import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def functionD(pattern):
    num = int(pattern)
    num *= 2
    if num >= 10000:
        num %= 10000
    new_pattern = str(num)
    new_pattern = '0' * (4 - len(new_pattern)) + new_pattern
    return new_pattern


def functionS(pattern):
    num = int(pattern)
    if num == 0:
        return '9999'
    num -= 1
    new_pattern = str(num)
    new_pattern = '0' * (4 - len(new_pattern)) + new_pattern
    return new_pattern


def functionL(pattern):
    new_pattern = pattern[1] + pattern[2] + pattern[3] + pattern[0]
    return new_pattern


def functionR(pattern):
    new_pattern = pattern[3] + pattern[0] + pattern[1] + pattern[2]
    return new_pattern


def bfs(start, goal):
    q = deque([[start, '']])
    while q:
        now_start, ans = q.popleft()
        num = int(now_start)
        num *= 2
        if num >= 10000:
            num %= 10000
        new_pattern = str(num)
        new_pattern = '0' * (4 - len(new_pattern)) + new_pattern
        ans1 = ans + 'D'
        if new_pattern == goal:
            return ans1
        else:
            q.append([new_pattern, ans1])

        num = int(now_start)
        if num == 0:
            new_pattern = '9999'
        else:
            num -= 1
            new_pattern = str(num)
            new_pattern = '0' * (4 - len(new_pattern)) + new_pattern
        ans2 = ans + 'S'
        if new_pattern == goal:
            return ans2
        else:
            q.append([new_pattern, ans2])

        new_pattern = now_start[1] + now_start[2] + now_start[3] + now_start[0]
        ans3 = ans + 'L'
        if new_pattern == goal:
            return ans3
        else:
            q.append([new_pattern, ans3])

        new_pattern = now_start[3] + now_start[0] + now_start[1] + now_start[2]
        ans4 = ans + 'R'
        if new_pattern == goal:
            return ans4
        else:
            q.append([new_pattern, ans4])

sys.stdin = open('input.txt')
for T in range(int(input())):
    start, goal = map(str, input().split())
    start = '0' * (4-len(start)) + start
    goal = '0' * (4-len(goal)) + goal
    print(bfs(start, goal))
