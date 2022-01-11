import sys
sys.stdin = open('input.txt')

# 백트래킹
# 최소한의 교체 횟수로 목적지에 도착하기
# 출발지에서 배터리 장착은 교환횟수에서 제외

def charger(idx, count):
    global result

    if count >= result:
        return

    # 목적지를 넘고
    if idx >= STOP:
        # 최솟값 갱신
        result = count
        return

    # 2 3 1 1
    for i in range(stations[idx], 0, -1): # 2 1
        charger(idx+i, count+1)

t = int(input())
for tc in range(1, t+1):
    stations = list(map(int, input().split()))
    STOP = stations[0] - 1 # 5-1 = 4
    stations = stations[1:] # 2 3 1 1

    result = float('inf')

    # 처음 count는 1로 안치니 -1부터 시작
    charger(0, -1)
    print('#{} {}'.format(tc, result))
