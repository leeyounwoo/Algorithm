from collections import deque
from itertools import combinations
from copy import deepcopy


def overlap(rect1, rect2):
    return not (rect1[2] < rect2[0] or rect1[0] > rect2[2] or rect1[1] > rect2[3] or rect1[3] < rect2[1])


def check(mark):
    indexs = [i for i in range(len(mark))]
    for com in combinations(indexs, 2):
        flag = overlap(mark[com[0]], mark[com[1]])
        if flag:
            return False

    return True


def move_left(mark):
    x1, y1, x2, y2 = mark[0], mark[1], mark[2], mark[3]
    if x1 - 1 >= 0:
        return [x1 - 1, y1, x2 - 1, y2]
    else:
        return False


def move_right(mark):
    x1, y1, x2, y2 = mark[0], mark[1], mark[2], mark[3]
    if x2 + 1 <= 32767:
        return [x1 + 1, y1, x2 + 1, y2]
    else:
        return False


def move_up(mark):
    x1, y1, x2, y2 = mark[0], mark[1], mark[2], mark[3]
    if y2 + 1 <= 32767:
        return [x1, y1 + 1, x2, y2 + 1]
    else:
        return False


def move_down(mark):
    x1, y1, x2, y2 = mark[0], mark[1], mark[2], mark[3]
    if y1 - 1 >= 0:
        return [x1, y1 - 1, x2, y2 - 1]
    else:
        return False


def bfs(mark):
    result = 0
    visited = []
    visited.append(mark)
    if check(mark):
        return result

    q = deque([[result, mark]])

    while q:
        cnt, now_mark = q.popleft()

        if check(now_mark):
            return cnt

        for i in range(len(now_mark)):
            t1 = move_left(now_mark[i])
            t2 = move_right(now_mark[i])
            t3 = move_up(now_mark[i])
            t4 = move_down(now_mark[i])

            if t1:
                new_mark1 = deepcopy(now_mark)
                new_mark1.pop(i)
                new_mark1.insert(i, t1)
                if new_mark1 not in visited:
                    q.append([cnt + 1, new_mark1])

            if t2:
                new_mark2 = deepcopy(now_mark)
                new_mark2.pop(i)
                new_mark2.insert(i, t2)
                if new_mark2 not in visited:
                    q.append([cnt + 1, new_mark2])

            if t3:
                new_mark3 = deepcopy(now_mark)
                new_mark3.pop(i)
                new_mark3.insert(i, t3)
                if new_mark3 not in visited:
                    q.append([cnt + 1, new_mark3])

            if t4:
                new_mark4 = deepcopy(now_mark)
                new_mark4.pop(i)
                new_mark4.insert(i, t4)
                if new_mark4 not in visited:
                    q.append([cnt + 1, new_mark4])


def solution(N, L):
    mark = []
    for i in range(N):
        xy = L[i]
        left, right, up, down = xy[0], xy[2], xy[1], xy[3]
        if left > right:
            mark.append([right, up, left, down])
        else:
            mark.append([left, down, right, up])

    return bfs(mark)

print(solution(3, [[5,7,6,6],[3,9,5,4],[8,2,7,6]]))