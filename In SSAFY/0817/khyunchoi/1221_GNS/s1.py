import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    tc_num, tc_length = input().split()
    num_list = list(input().split())
    alien_dict = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}
    alien_key_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    for num in num_list:
        alien_dict[num] += 1

    print('#{}'.format(tc))
    for key in alien_key_list:
        for i in range(alien_dict[key]):
            print(key, end=' ')
    print()