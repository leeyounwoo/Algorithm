import sys
sys.stdin = open('input.txt')


for T in range(1, 1+int(input())):
    N, M = map(int, input().split())
    # 0번째: 흰색, 1번째: 파란색, 2번째: 빨간색
    flag_color = [[0, 0, 0] for _ in range(N)]
    for i in range(N):
        temp = list(input())
        flag_color[i][0] = temp.count('W')
        flag_color[i][1] = temp.count('B')
        flag_color[i][2] = temp.count('R')
    # 가장 위엔 흰색이어야 하고 가장 아래는 빨간색이어야 함
    fix = (M - flag_color[0][0]) + (M - flag_color[N-1][2])

    # 경우의 수를 나타내는 저장하는 color_list 리스트
    color_list = []
    for start_one in range(N-2):
        color = [-1] * (N-2)
        for zero in range(start_one):
            color[zero] = 0
        for two in range(N-2, start_one, -1):
            for one_two in range(start_one, N-2):
                if one_two < two:
                    color[one_two] = 1
                else:
                    color[one_two] = 2
            color_list.append(color[:])


    min_variable = (N-2) * M
    for colors in color_list:
        temp_sum = 0
        for i in range(len(colors)):
            temp_sum += (M - flag_color[i+1][colors[i]])

        if temp_sum < min_variable:
            min_variable = temp_sum
    ans = fix + min_variable
    print('#{} {}'.format(T, ans))



