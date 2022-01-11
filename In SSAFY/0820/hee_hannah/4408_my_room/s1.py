import sys
sys.stdin = open('input.txt')

def div(num):
    return (int(num) + 1) // 2



T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 돌아갈 사람의 수
    # 큰방에서 작은 방으로 돌아갈수도잇다..

    students = [list(map(div, input().split())) for _ in range(N)] # 복도값
    road = [0] * 201
    for i in range(N):
        if students[i][0] > students[i][1]: # 현재 있는 복도가 돌아갈 복도보다 크다면
            students[i][0], students[i][1] = students[i][1], students[i][0]

        for j in range(students[i][0], students[i][1]+1): # 도착점까지
            road[j] += 1
    print('#{} {}'.format(tc, max(road))) # 가장 많이 지나치는 복도의수 카운트인듯

