import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    nums = [i for i in range(1, 13)]

    cnt = 0
    for i in range(1 << 12):

        tmp = []
        for j in range(12):
            if i & (1 << j):
                tmp.append(nums[j])

        tmp_len = 0
        tmp_sum = 0
        for j in tmp:
            tmp_len += 1
            tmp_sum += j

        if tmp_len == N and tmp_sum == K:
            cnt += 1

    print('#{} {}'.format(tc, cnt))