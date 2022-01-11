import sys
sys.stdin = open('input.txt')


for T in range(1, 1+int(input())):
    N = int(input())
    requests = []
    for i in range(N):
        start, end = map(int, input().split())
        time = end - start
        requests.append((start, end))
    # print(requests)
    sorted_requests = sorted(requests, key=lambda x: (x[1]-x[0]))
    check = [False] * 25
    ans = len(requests)
    for start, end in sorted_requests:
        for time in range(start, end):
            if check[time]:
                ans -= 1
                break
        else:
            for time in range(start, end):
                check[time] = True
    print('#{} {}'.format(T, ans))