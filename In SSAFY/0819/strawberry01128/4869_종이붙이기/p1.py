import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    print('#{} {}'.format(test_case,2**((N /10)-1)))
