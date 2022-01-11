import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(T):
    N = int(input())
    result = [[1]]

    for _ in range(1, N):
        arr = [1]
        for j in range(len(result[-1])-1):
            sum_arr = 0
            for k in range(2):
                sum_arr += result[-1][j+k]
            arr.append(sum_arr)
        arr.append(1)
        result.append(arr)

    print('#{}'.format(tc+1))
    for i in result:
        print(*i)
