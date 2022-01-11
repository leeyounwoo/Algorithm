import sys

sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    number_len, number_add = map(int, input().split())
    number = list(map(int, input().split()))
    result_a = []
    for number_test in range(number_len - number_add + 1):
        result_a.append(number[number_test]+number[number_test+1]+number[number_test+2])
    print(f'#{test_case} {max(result_a)-min(result_a)}')
