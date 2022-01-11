import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    station_list = [0] * (N + 1)
    charge_count = 0

    #충전소 위치에 1넣기
    for i in range(len(station)):
        station_list[station[i]] += 1

    start = 0
    end = K
    while True:
        energy = 0

        for i in range(start + 1, end + 1):#시작지점 ~ 한번 충전시 이동 가능한 거리 사이
            if station_list[i] == 1: #충전소에 들어가면 충전소 위치로 시작지점을 바꿔주고
                start = i
            else: #한 칸 이동할 때마다 에너지 1더해줌
                energy += 1

        #에너지가 K가 되면 count 0으로 하고 반복문 탈출
        if energy == K:
            charge_count = 0
            break

        charge_count += 1
        end = start + K

        if end >= N:
            break

    print('#{} {}'.format(tc+1, charge_count))