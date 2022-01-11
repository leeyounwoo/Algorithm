import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, M, K = map(int, input().split())
    people = list(map(int, input(). split()))
    people.sort() # 시간대별로 sort하여 차례대로 들어오게 만듦

    result = "Possible"
    for i in range(N):
        boong = (people[i] // M) * K - (i + 1)
        if boong < 0:
            result = "Impossible"
            break

    print("#{} {}".format(tc + 1, result))

# 자주 틀리는 요인 https://www.acmicpc.net/blog/view/70