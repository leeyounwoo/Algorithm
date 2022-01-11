import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    student_number = int(input())
    students = []
    road = []
    count = 1
    for i in range(student_number):
        students.append(list(map(int,input().split())))
    for k in range(student_number):
        for j in range(students[k][0], students[k][1]):
            if not j in road:
                road.append(j)
            else:
                count += 1
                break

    print('#{} {}'.format(test_case,count))

####################################
# 교수님의 방법

def div(num):
    return (int(num)+1) // 2

T = int(input())

for tc in range(1, T+1):
    N = int(input()) #돌아갈 사람의 수
    students = [list(map(div, input().split())) for _ in range(N)]

    road = [0] * 201

    for i in range(N):
        if students[i][0] > students[i][1]:
            students[i][0], students[i][1] = students[i][1], students[i][0]

        for j in range(students[i][0], students[i][1]+1):
            road[j] += 1
        print('#{} {}'.format(tc, max(road)))