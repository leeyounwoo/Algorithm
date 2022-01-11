import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N , M = map(int, (input().split()))

    str_list = [list(map(str, input().split())) for _ in range(N)]
    result = 0
    check_list = []
    cnt = 0

    while M-1+cnt < N:
        for chr_1 in str_list:
            for chr_2 in chr_1[cnt:M-1+cnt]:
                if chr_2 == chr_2[::-1]:
                    result = chr_2
        cnt += 1

    cnt = 0
    while cnt < N:
        for chr_3 in str_list:
            for chr_4 in chr_3[cnt]:
                check_list.append(chr_4)
                if result == 0 and cnt != 0 and check_list == check_list[::-1]:
                    result = check_list
        check_list = []
        cnt += 1

    print('#{0} {1}'.format(tc+1, result))
