import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    a, b = input().split()

    i = 0 # a의 인덱스
    n = len(a)
    m = len(b)
    count = 0 # 횟수
    while i < n:
        if a[i] == b[0]: # 첫 글자가 같고
            if a[i:i+m] == b: # 그게 b라면?
                i += m
                count += 1
        else:
            i += 1
            count += 1

    print('#{0} {1}'.format(tc, count))