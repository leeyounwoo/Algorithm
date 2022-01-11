import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    num = int(input())
    len_num = num*num

    number_list = list(range(1, len_num+1))
    check_list = [[0] * num for _ in range(num)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    now_status = 0
    x, y = 0, 0

    for