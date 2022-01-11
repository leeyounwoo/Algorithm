import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(TC):
    num = int(input())
    num_lst = list(map(int, input().split()))

    my_max = 0
    my_min = 1000001

    for n in num_lst:
        if n > my_max:
            my_max = n
        if my_min > n:
            my_min = n

    sub = max(num_lst) - min(num_lst)

    print(f"#{tc+1} {sub} {my_max-my_min}")

