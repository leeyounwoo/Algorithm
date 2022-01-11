import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    a = [2, 3, 5, 7, 11]  # 나눌 수로 리스트를 만듭니다.
    divide_num = [0]*5  # 값을 넣을 리스트를 만듭니다.
    for i in range(len(a)):
        while num % a[i] == 0:  # 2, 3, 5, 7, 11
            divide_num[i] += 1  # 나눌때마다 수를 하나씩 더해 줍니다.
            num = num // a[i] # num을 나눠줍니다.
    print('#{} {} {} {} {} {}'.format(tc, divide_num[0], divide_num[1], divide_num[2], divide_num[3], divide_num[4]))


