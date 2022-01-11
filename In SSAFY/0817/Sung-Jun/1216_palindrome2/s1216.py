import sys
sys.stdin = open('input.txt')

T = 10

for _ in range(T):
    tc = int(input())
    numbers = [input() for _ in range(100)]

    len_max = 0
    for i in range(len(numbers)):
        for j in range(len(numbers[0])):
            # 가로 검사
            for num in range(1, len(numbers[0])-j+1):
                check_num = numbers[i][j:j+num+1]
                if len(check_num) >= 2 and check_num == check_num[::-1]:
                    if len_max < len(check_num):
                        len_max = len(check_num)

    #세로검사
    for j in range(len(numbers[0])):
        for i in range(len(numbers)):
            check_num = ''
            for num in range(len(numbers)-i):
                check_num += numbers[i+num][j]
                if len(check_num) >= 2 and check_num == check_num[::-1]:
                    if len_max < len(check_num):
                        len_max = len(check_num)
    print('#{} {}'.format(tc, len_max))