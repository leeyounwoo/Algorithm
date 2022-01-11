import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()

    cnt = {}

    for s in str2:
        if s in str1:
            if s in cnt.keys():
                cnt[s] += 1
            else:
                cnt[s] = 1

    max_cnt = 0

    for c in cnt.values():
        if c > max_cnt:
            max_cnt = c

    print('#{} {}'.format(t, max_cnt))
