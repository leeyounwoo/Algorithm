import sys
sys.stdin = open("input.txt")

T = int(input())

# 버스가 가면서 배터리 충전하는 함수
# idx는 정류장의 위치, cnt는 충전횟수
def bus(idx, cnt):
    global result
    # 시간초과를 피하기 위해서 더 작은 값이 안나오면 중지
    if cnt > result:
        return
    # 만약 목적지를 넘는다면
    if idx >= N:
        # 지금까지 센 횟수를 리턴하자
        result = cnt
        return
    # 한번 충전해서 갈 수 있는 곳을 다 둘러보는 반복문
    for i in range(station[idx], 0, -1):
        # 그 경우의 수에 해당하는곳에서 재귀
        bus(idx+i, cnt + 1)

for tc in range(1, T+1):
    station = list(map(int, input().split()))
    # 0부터 시작하니까 -1
    N = station.pop(0) - 1
    result = 10000
    # 첫 정류장 제외 -> cnt에 -1을 넣어준다.
    bus(0, -1)

    print("#{} {}".format(tc, result))