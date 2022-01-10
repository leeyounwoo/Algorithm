import sys


def input():
    return sys.stdin.readline().rstrip()


def makeQuadTree(n, temp):
    global ans
    flag = 0
    for i in range(n):
        for j in range(n):
            if temp[i][j] == '1':
                flag += 1
    if flag == n * n:
        ans += '1'
        return
    elif flag == 0:
        ans += '0'
        return
    else:
        new_1 = []
        new_2 = []
        new_3 = []
        new_4 = []
        mid = n // 2
        for i in range(n):
            if i < mid:
                new_1.append(temp[i][:mid])
                new_2.append(temp[i][mid:])
            else:
                new_3.append(temp[i][:mid])
                new_4.append(temp[i][mid:])

        ans += '('
        makeQuadTree(n//2, new_1)
        makeQuadTree(n//2, new_2)
        makeQuadTree(n//2, new_3)
        makeQuadTree(n//2, new_4)
    ans += ')'


sys.stdin = open('input.txt')
n = int(input())
graph = [list(input()) for _ in range(n)]

ans = ''
makeQuadTree(n, graph)
print(ans)