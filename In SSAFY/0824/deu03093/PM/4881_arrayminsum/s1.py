import sys
sys.stdin = open('input.txt')


def minsum(numbers, arr):
    if len(arr) == N:
        temp = 0
        for i in range(len(numbers)):
            temp += numbers[i][arr[i]]
        ans.append(temp)
        return

    for i in range(N):
        if i not in arr:
            arr.append(i)
            minsum(numbers, arr)
            arr.pop()




for T in range(1, 1+int(input())):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    minsum(numbers, [])
    print('#{} {}'.format(T, min(ans)))
