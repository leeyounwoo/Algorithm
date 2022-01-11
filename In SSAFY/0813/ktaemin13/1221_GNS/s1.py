import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    M, N = map(str, input().split())
    numbers = list(map(str, input().split()))

    num_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    cnt = 0
    for num in num_list:
        for i in range(cnt, int(N)):
            if num == numbers[i]:
                numbers[cnt], numbers[i] = numbers[i], numbers[cnt]
                cnt += 1

    print('#{0}'.format(tc+1), *numbers)