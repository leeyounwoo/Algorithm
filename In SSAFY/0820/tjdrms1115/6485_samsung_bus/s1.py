import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T + 1):

    # 변수들을 초기화합니다.
    N = int(input())
    route_list = []
    for _ in range(N):
        route_list.append(list(map(int, input().split())))
    P = int(input())
    station_list = []
    for _ in range(P):
        station_list.append(int(input()))

    # 정거장을 지나친 횟수를 저장할 리스트를 만듧니다. 최대 크기로 고정합니다.
    station_count = [0] * 5001

    # 버스가 지나간 정거장의 위치에 지나간 횟수를 1회 더합니다.
    for a, b in route_list:
        for i in range(a, b + 1):
            station_count[i] += 1

    # 정거장별로 버스가 지나간 횟수를 조회해 결과를 저장합니다.
    result = []
    for station in station_list:
        result.append(station_count[station])

    # 출력합니다.
    result = ' '.join(map(str, result))
    answer.append(result)

for tc in range(1, T + 1):
    print('#{} {}'.format(tc, answer[tc - 1]))
