import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    result = [0] * 10

    for i in range(10//2):
        result[i * 2] = num_list.pop(num_list.index(max(num_list)))
        result[i * 2 + 1] = num_list.pop(num_list.index(min(num_list)))

    print('#{}'.format(tc), *result[:10])