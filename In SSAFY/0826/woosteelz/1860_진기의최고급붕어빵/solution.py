import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort()
    bread = [0 for _ in range(max(customer) + 1)]
    ans = 'Possible'
    cnt = 0

    for i in range(1, len(bread)):
        if i % M == 0:
            bread[i] = bread[i-1] + K
        else:
            bread[i] = bread[i-1]

    while customer:
        curr = customer.pop(0)
        cnt += 1
        if bread[curr] < cnt:
            ans = 'Impossible'
            break

    print('#{} {}'.format(tc+1, ans))