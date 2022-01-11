import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    temp = list(map(int, input().split()))
    N = temp[0]
    battery = [0] + temp[1:]

    # 현재 정류장에서 충전해서 최대 어디까지 갈 수 있는지 저장
    max_station = [0 for _ in range(N)]
    for i in range(N):
        max_station[i] = i + battery[i]

    cnt = -1 # 1번 정류장에서 장착은 교환횟수에서 제외
    target = N
    j = 1
    while target > 1:
        if max_station[j] >= target:
            cnt += 1
            target = j
            j = 1
        else:
            j += 1
    
    print('#{} {}'.format(t, cnt))
