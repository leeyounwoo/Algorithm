import sys
sys.stdin = open("input.txt")
T = int(input())
output = {0:'ZRO', 1:'ONE', 2:'TWO', 3:'THR', 4:'FOR', 5:'FIV', 6:'SIX', 7:'SVN', 8:'EGT', 9:'NIN'}
numbers = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

for tc in range(1, T+1):
    N = list(input().split())
    input_numbers = list(input().split())
    for i in range(len(input_numbers)):
        input_numbers[i] = numbers[input_numbers[i]]
    input_numbers.sort()
    for j in range(len(input_numbers)):
        input_numbers[j] = output[input_numbers[j]]
    print('{} {}'.format(N[0], ' '.join(input_numbers)))


