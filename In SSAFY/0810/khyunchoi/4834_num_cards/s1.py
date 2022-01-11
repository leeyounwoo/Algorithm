import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))
    num_cnt = [0] * 10

    for card in cards:
        num_cnt[card] += 1

    max_num_cnt = num_cnt[0]
    for cnt in num_cnt:
        if max_num_cnt < cnt:
            max_num_cnt = cnt

    for i in range(9, -1, -1):
        if num_cnt[i] == max_num_cnt:
            print('#{} {} {}'.format(tc, i, num_cnt[i]))
            break