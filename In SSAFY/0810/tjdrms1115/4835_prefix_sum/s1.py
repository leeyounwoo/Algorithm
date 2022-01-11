import sys
sys.stdin = open('input.txt')

T = int(input())

answer = []
for tc in range(1, T+1):

    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    sum_list = [0] * (N-M+1)

    for i in range(N-M+1):
        for j in range(M):
            sum_list[i] += numbers[i+j]

    sum_max = 0
    sum_min = 10000000
    for i in range(len(sum_list)):
        if sum_min > sum_list[i]:
           sum_min = sum_list[i]
        if sum_max < sum_list[i]:
           sum_max = sum_list[i]


    answer.append(sum_max - sum_min)


for tc in range(1, T+1):
    print('#{0} {1}'.format(tc, answer[tc-1]))