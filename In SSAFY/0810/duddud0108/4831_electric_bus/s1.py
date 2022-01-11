import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    K, N, M = map(int, input().split())
    charge_num = 0
    station_list = [0] + list(map(int, input().split())) + [N]

    max_station = K
    i = 1
    while max_station < N:
        if station_list[i]-station_list[i-1] > K: # 충전소의 간격이 최대 이동 거리를 넘으면 break
            charge_num = 0
            break

        if station_list[i] > max_station:
            charge_num += 1
            max_station = station_list[i-1] + K
        elif station_list[i] == max_station:
            charge_num += 1
            max_station = station_list[i] + K
        i += 1

    print('#{0} {1}'.format(tc+1, charge_num))

