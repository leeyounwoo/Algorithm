import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 1, 2번 연산
    pascal = [[1], [1, 1]]
    for i in range(2, N):
        # 맨 첫번째는 반드시 1
        arr = [1]
        #위쪽 2개의 값을 더하면 아래 값이 나온다.
        for j in range(i-1):
            arr += [pascal[i - 1][j] + pascal[i - 1][j + 1]]
        # 마지막은 반드시 1
        arr += [1]
        pascal += [arr]

    print("#{}".format(tc))
    for i in range(N):
        print(*pascal[i])