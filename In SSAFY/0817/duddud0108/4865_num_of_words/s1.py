import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()

    max_cnt = 0
    for i in set(str1):
        cnt = str2.count(i)
        if cnt > max_cnt:
            max_cnt = cnt
    print('#{0} {1}'.format(tc+1, max_cnt))


