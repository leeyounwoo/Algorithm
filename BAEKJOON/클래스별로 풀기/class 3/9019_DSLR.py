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
    q = deque([[start, goal, '']])
    while q:
        now_start, now_goal, ans = q.popleft()
        n1 = functionD(now_start)
        ans1 = ans + 'D'
        if n1 == now_goal:
            return ans1
        else:
            q.append([n1, now_goal, ans1])

        n2 = functionS(now_start)
        ans2 = ans + 'S'
        if n2 == now_goal:
            return ans2
        else:
            q.append([n2, now_goal, ans2])

        n3 = functionL(now_start)
        ans3 = ans + 'L'
        if n3 == now_goal:
            return ans3
        else:
            q.append([n3, now_goal, ans3])

        n4 = functionR(now_start)
        ans4 = ans + 'R'
        if n4 == now_goal:
            return ans4
        else:
            q.append([n4, now_goal, ans4])

sys.stdin = open('input.txt')
for T in range(int(input())):
    start, goal = map(str, input().split())
    start = '0' * (4-len(start)) + start
    goal = '0' * (4-len(goal)) + goal
    print(bfs(start, goal))
