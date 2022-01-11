import sys
sys.stdin = open('input.txt')
t = int(input())

arr = [i for i in range(1, 13)]
length = len(arr)
for tc in range(1, t+1):
    n, k = map(int, input().split())
    answer = 0

    for i in range(1 << n):
        result = 0
        answer = []
        for j in range(n):
            if i & (1 << j):
                result += arr[j]
                answer.append(arr[j])
    for x

    print(answer)
