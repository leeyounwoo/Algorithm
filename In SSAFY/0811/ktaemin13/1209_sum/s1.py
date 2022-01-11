import sys
sys.stdin = open('input.txt')

TC = 10
for tc in range(1, TC+1):
    lst = []
    N = int(input())
    for i in range(100):
        sub_lst = list(map(int, input().split()))
        lst.append(sub_lst)

    result = 0

    for i in range(100):             # 열의 합
        max = 0
        for j in range(100):
            max += lst[i][j]

        if max > result:
            result = max
        
    for i in range(100):             # 행의 합
        max = 0
        for j in range(100):
            max += lst[j][i]

        if max > result:
            result = max

    max = 0

    for i in range(100):             # 대각선(\) 합
       max += lst[i][i]

    if max > result:
        result = max

    max = 0

    for i in range(100):             # 대각선(/) 합
        max += lst[i][99-i]

    if max > result:
        result = max

    print('#{0} {1}'.format(tc,result))