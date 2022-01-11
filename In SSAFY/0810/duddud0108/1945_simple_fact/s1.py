import sys
sys.stdin = open('input.txt')

lst = [2, 3, 5, 7, 11]
T = int(input())

for tc in range(T):
    N = int(input())
    result = []

    for i in lst:
        count = 0
        while True:
            if N % i == 0:
                N /= i
                count += 1
            else:
                break
        result.append(count)

    print('#{0}'.format(tc+1), *result)
