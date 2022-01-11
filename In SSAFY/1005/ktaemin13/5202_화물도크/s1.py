import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split()))for _ in range(N)]

    sorted_info = sorted(info, key=lambda x: x[1])  # 종료 시간을 기준으로 정렬
    print(sorted_info)
    cnt = 0
    now = 0  # 현재 반복문의 종료 시간
    # 돌면서 검사
    for i in range(N):
        s = sorted_info[i][0]  # 시작 시간
        e = sorted_info[i][1]  # 종료 시간
        if now <= s:  # 종료 시간이 시작시간과 겹치지 않는다면,
            cnt += 1
            now = e

    print("#{} {}".format(tc, cnt))

