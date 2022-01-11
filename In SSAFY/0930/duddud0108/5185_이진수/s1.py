import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, nums = input().split()
    result = ''
    for i in range(int(N)):
        num = int(nums[i], 16)
        num = format(num, 'b')
        while len(num2) != 4:
            num2 = '0'+ num
        result += num
    print('#{} {}'.format(tc, result))