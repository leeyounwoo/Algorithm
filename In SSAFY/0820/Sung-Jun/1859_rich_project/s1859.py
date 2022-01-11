import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    product = list(map(int, input().split()))

    max = product[-1]
    result = 0
    for num in range(N-2, -1, -1):
        if max > product[num]:
            result += max - product[num]
        else:
            max = product[num]
    print('#{} {}'.format(tc+1, result))
