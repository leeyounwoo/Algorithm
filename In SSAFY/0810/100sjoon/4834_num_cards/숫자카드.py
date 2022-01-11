import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))

    mx_num = numbers[0]
    for k in numbers:
        if k > mx_num:
            mx_num = k

    cnt_list = [0] * (mx_num+1) # 카운팅 빈배열 만들기
    for i in range(0, N):
        cnt_list[numbers[i]] += 1

    mx_cnt = 0
    mx_num_2 = 0
    for j in range(0, len(cnt_list)):
        if cnt_list[j] >= mx_cnt: #cnt값이 같아도 더 값이 큰 것 출력
            mx_cnt = cnt_list[j]
            mx_num_2 = j

    print("#{} {} {}".format(tc, mx_num_2, mx_cnt))