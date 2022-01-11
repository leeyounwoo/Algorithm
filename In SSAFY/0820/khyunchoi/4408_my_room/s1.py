import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    students = []
    rooms = [0] * 201
    
    for i in range(N):
        start, end = map(int, input().split())
        students.append([(start+1)//2, (end+1)//2])

    for student in students:
        if student[1] < student[0]:
            student[0], student[1] = student[1], student[0]

    for student in students:
        for i in range(student[0], student[1]+1):
            rooms[i] += 1

    print('#{} {}'.format(tc, max(rooms)))