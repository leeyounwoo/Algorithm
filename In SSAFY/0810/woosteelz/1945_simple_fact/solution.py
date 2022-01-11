import sys
sys.stdin = open('input.txt')

TC = int(input())
factors = [2, 3, 5, 7, 11]
for tc in range(TC):
    ans = ''
    num = int(input())
    for factor in factors:
        temp = 0
        while True:
            if num % factor == 0:
                num //= factor
                temp += 1
            else:
                break
        ans += str(temp) + ' '
    print('#{} {}'.format(tc+1, ans))
