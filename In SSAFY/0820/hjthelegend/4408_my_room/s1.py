import sys

sys.stdin = open('input.txt')

def div(num):
    return int(num+1) // 2


t = int(input())

for tc in range(1, t+1):
    n = int(input())

    students = [list(map(int, input().split())) for _ in range(n)]

    road = [0] * 201

    for i in range(n):
        if students[i][0] > students[i][1]:
            students[i][0], students[i][1] = students[i][1], students[i][0]

        for j in range(students[i][0], students[i][1]+1):
            road[j] += 1

        print('#{} {}'.format(tc, max(road)))