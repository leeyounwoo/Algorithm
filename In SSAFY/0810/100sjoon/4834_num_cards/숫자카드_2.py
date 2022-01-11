import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    numbers = list(map(int, input()))

    mx_num = 0
    mx_cnt = 0
    for i in range(10):
        if numbers.count(i) >= mx_cnt:
            mx_cnt = numbers.count(i)
            mx_num = i

    print("#{} {} {}".format(tc, mx_num, mx_cnt))