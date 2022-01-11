import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    max_sum = 0
    for i in range(len(arr)-M+1):
        for j in range(len(arr[i])-M+1):
            sum = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    sum += arr[x][y]
            if sum > max_sum:
                max_sum = sum

    print(f'#{t} {max_sum}')