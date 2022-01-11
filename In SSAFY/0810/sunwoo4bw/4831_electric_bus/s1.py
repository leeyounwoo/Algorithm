import sys
sys.stdin = open('input.txt')
# 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지

T = int(input())
for tc in range(1, T+1):
    # k 한번 충전으로 최대 이동 수 n 종점 m 충전기 보유 정류장 수
    K, N, M = map(int, input().split())

    # 충전기 보유 정류장 위치
    charger_spot = list(map(int, input().split()))

    now = 0
    drive = K
    charge = 0
    while True:
        if drive== 0:
            charge = 0
            break

        if now + drive in charger_spot :
            now += drive
            charge += 1
            drive = K
        elif now + K >= N:
            break
        else:
            drive -= 1

    print('#{} {}' .format(tc, charge))


