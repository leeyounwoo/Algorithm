import sys
sys.stdin = open('input.txt')


def charge(location, count):
    global result
    # 더 작은 값이 안나오면 중지
    if count >= result:
        return

    # 만약 목적지를 넘는다면
    if location >= N - 1:
        # 지금 센 횟수랑 결과값이랑 비교해서 작다면 갱신
        if count <= result:
            result = count
        return
    # 한번 충전해서 갈수 있는 곳을 다 둘러보는 반복문
    # 해당 정류장에서 해당하는 배터리로 갈수 있는 경우의 수를 모두 둘러본다.
    for i in range(battery[location]):
        # 그 경우의 수에 해당하는곳으로 옮겨서 다시 살펴보자
        # i가 0부터 시작하니까 1씩 더 더한다.
        charge(location+i+1, count+1)


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    battery = arr[1:]
    result = 101
    charge(0, -1)
    print('#{} {}'.format(tc, result))
