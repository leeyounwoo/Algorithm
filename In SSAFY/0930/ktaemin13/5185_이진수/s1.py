import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, hex_num = input().split()
    dec_num = int(hex_num, 16)  # 16진수 = > 10진수
    bin_num = format(dec_num, 'b')  # 10진수 => 2진수
    if len(bin_num) < int(N) * 4:  # 2진수의 맨 앞자리에 0 붙여주기
        bin_num = '0'+bin_num

    print('#{} {}'.format(tc, bin_num))
