import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    min_num = 1000001
    max_num = 0
    for num in numbers:
        if min_num > num:
            min_num = num
        if max_num < num:
            max_num = num

    answer.append(max_num - min_num)

for tc in range(1, T+1):
    print('#{0} {1}'.format(tc, answer[tc-1]))
