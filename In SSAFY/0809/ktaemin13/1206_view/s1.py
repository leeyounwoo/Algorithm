import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    apt = list(map(int, input().split()))

    cnt = 0
    for i in range(2, N-2):
        if apt[i]-1 >= apt[i-1] and apt[i]-1 >= apt[i-2] and apt[i]-1 >= apt[i+1] and apt[i]-1 >= apt[i+2]:
            cnt += 1
            for j in range(2, apt[i]+1):
               if apt[i] - j >= apt[i - 1] and apt[i] - j >= apt[i - 2] and apt[i] - j >= apt[i + 1] and apt[i] - j >= apt[i + 2]:
                   cnt += 1



    print('#{0} {1}'.format(tc+1,cnt))