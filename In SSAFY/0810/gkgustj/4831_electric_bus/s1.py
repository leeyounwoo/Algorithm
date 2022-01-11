import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    '''
    K : 한 번 충전으로 최대 이동 횟수
    N : 종점
    M : 충전기 설치된 정류장 수
    '''
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))

    energy = K
    cnt = 0
    bus = 0

    while True:
        bus += 1
        energy -= 1

        if bus in station :
            if bus == station[0] :
                station.pop(0)
                # 다음 정류장이 없으면 종점 추가
                if not station :
                    station.append(N)

            # 다음 정류장과 최대 이동 횟수 비교해서 충전
            if energy < station[0]-bus :
                energy = K
                cnt += 1

        if bus == N : # 버스가 종점에 도착
            break
        elif not energy : # 도착하기 전에 이동 횟수 소진
            cnt = 0
            break

    print(f'#{t} {cnt}')