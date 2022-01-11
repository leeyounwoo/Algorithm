import sys

sys.stdin = open('input.txt')
for T in range(1, int(input()) + 1):
    drive, goal, stop_num = map(int, input().split())
    # 출발지점부터 도착지점까지 모든 정류장을 0으로 초기화
    stops = [0] * (goal + 1)
    charge_stops = list(map(int, input().split()))
    # 충전소가 있으면 1로 바꿔줌
    for i in charge_stops:
        stops[i] = 1

    # 현재 위치
    now = 0
    # 충전횟수
    count = 0
    # 다음 충전소까지 이동할 수 있는지 여부
    flag = 1
    while flag and now < goal:
        # (가능한 가장 멀리 있는 정류장) ~ (현재 위치 + 1)
        for i in range(now + drive, now, -1):
            if stops[i]:
                now = i
                count += 1
                # 도착지에 도달가능
                if i + drive + 1 > goal:
                    flag = 0
                break
        # 현재 위치 + 1까지 왔는데도 충전소가 없는 경우
        else:
            count = 0
            break

    print('#{} {}'.format(T, count))

