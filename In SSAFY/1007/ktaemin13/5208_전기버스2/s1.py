import sys
sys.stdin = open("input.txt")

T = int(input())

def bus(idx, cnt):
    global result
    if cnt >= result:
        return
    if idx >= N - 1:
        if cnt <= result:
            result = cnt
        return
    for i in range(info[idx]):
        bus(idx+i+1, cnt + 1)


for tc in range(1, T+1):
    info = list(map(int, input().split()))
    N = info.pop(0)
    result = float('inf')
    bus(0, 0)
    print("#{} {}".format(tc, result-1))  # 처음 충전은 세지 않음
