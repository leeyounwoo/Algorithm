import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    case = list(input().split())
    numbers = list(input().split())
    tc = case[0]
    case_len = int(case[1])

    diff_num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    check = [0]*len(diff_num)
    for number in numbers:
        for ck in range(len(diff_num)):
            if number == diff_num[ck]:
                check[ck] += 1
    print(tc)
    for result in range(len(diff_num)):
        print('{} '.format(diff_num[result]) *check[result], end=' ')
    print()