import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = []

    # 가로줄 확인
    garo_list = []
    for i in range(N):
        data = input()
        garo_list.append(data)
        for i in range(len(data)-M+1):
            if data[i:M+i] == data[i:M+i][::-1]:
                result.append(data[i:M+i])

    # 세로줄 확인
    sero_list = []
    sero_sub_list = ''
    for x in range(N):
        for y in garo_list:
            sero_sub_list += y[x]
        sero_list.append(sero_sub_list)
        sero_sub_list = ''

    for sero_data in sero_list:
        for j in range(len(sero_data)-M+1):
            if sero_data[j:M+j] == sero_data[j:M+j][::-1]:
                result.append(sero_data[j:M+j])

    print('#{} {}'.format(tc, result[0]))