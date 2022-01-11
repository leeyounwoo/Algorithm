import sys
sys.stdin = open('input.txt')

# 최대 몇 대의 화물차가 이용 가능
# 얘도 정렬
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]
    time_s = sorted(time, key=lambda t : t[-1])
    # [[4,14], [8, 18], [17, 29], [20, 23], [23, 24]]

    total = 0
    re_start = 0             # 14
    for i in range(N):
        start = time_s[i][0] # 4
        end = time_s[i][1] # 14

        if re_start <= start:
            # 작업 가능
            total += 1
            re_start = end



    print('#{} {}'.format(tc, total))