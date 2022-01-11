import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    students = [list(map(int, input().split())) for _ in range(N)]

    rooms = [0 for _ in range(201)]

    for student in students:
        if student[1] > student[0]:
            for i in range((student[0]+1)//2, (student[1]+1)//2+1):
                rooms[i] += 1
        else:
            for i in range((student[1]+1)//2, (student[0]+1)//2+1):
                rooms[i] += 1

    result = rooms[0]
    for i in range(len(rooms)):
        if rooms[i] > result:
            result = rooms[i]

    print('#{0} {1}'.format(tc, result))