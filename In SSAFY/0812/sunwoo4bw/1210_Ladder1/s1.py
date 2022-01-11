import sys
sys.stdin = open('input.txt')

# 인덱스를 활용해서 방향전환을 하고 싶을 때는 dr, dc리스트를 만들고 접근
# 2에서 출발할 거야
# 위, 오, 왼
dr = [-1, 0, 0]
dc = [0, 1, -1]

T = 10
for _ in range(1, T + 1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)] # 100 * 100

    # 도착지점(2) 인덱스 구해줘
    for col in range(len(ladder)) :
        if ladder[99][col] == 2 :
            curr_c = col
    curr_r = 99

    # 방향 경우의 수
    while curr_r > 0 :
        if 0 <= curr_c + 1 <= 99 and ladder[curr_r][curr_c + 1] == 1:
            ladder[curr_r][curr_c + 1] = -1
            curr_c += 1

        elif 0 <= curr_c - 1 <= 99 and ladder[curr_r][curr_c - 1] == 1:
            ladder[curr_r][curr_c - 1] = -1
            curr_c -= 1

        elif 0 <= curr_r <= 99 and ladder[curr_r - 1][curr_c] == 1:
            ladder[curr_r - 1][curr_c] = -1
            curr_r -= 1

    print('#{} {}'.format(tc, curr_c))