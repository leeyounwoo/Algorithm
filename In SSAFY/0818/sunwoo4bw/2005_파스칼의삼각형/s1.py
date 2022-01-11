import sys
sys.stdin = open('input.txt')
# 파스칼의 삼각형 -> 콤비네이션
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 삼각형의 row
    pascal = [[1]] # first row

    for i in range(1, N) : # N=1일 땐 점프, 1- 1,2 - 1,2,3 - 1,2,...9
        temp = []
        for j in range(i+1): # i가 1일 때- 0 1, i가 2일 때- 0 1 2
            if j == 0 or j == i :
                temp.append(1)    # 양쪽이 1
            else :
                temp.append(pascal[i-1][j-1] + pascal[i-1][j])  # 내 윗줄에 있는 애들
        pascal.append(temp)

    print('#{}'.format(tc))
    for p in pascal :
        for n in p :
            print(n, end=' ')
        print()

