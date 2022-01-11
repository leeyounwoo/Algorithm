import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    bus_stop = list(map(int, input().split()))
    cnt = 0
    is_wrong = False
    # 거꾸로 N부터 출발해서 0에 도착하는 방식
    while N > 0:
        for i in range(N-K, N):      # N-K번째 부터 N번째 까지 버스정류장이 있는지 탐색
            if N-K <= 0:             # N-K가 0보다 작아졌다는 뜻은 도착했다는 뜻
                N = 0
                break

            if i in bus_stop:        # 버즈 정류장이 있으면 현재위치를 그 정류장으로 바꿔주고 충전횟수 +1
                cnt += 1
                N = i
                break
        else:                        # 만약 for문을 돌았는데 break가 안걸리면 정류장이 없단 뜻이므로
            is_wrong = True          # 종점에 도착할 수 없으므로 while문 종료
            break

    if is_wrong:                     # 종점에 도착하지 못했다면 충전횟수 0으로 초기화
        cnt = 0

    print('#{} {}'.format(tc, cnt))