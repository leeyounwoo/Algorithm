import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(str, input().split()))
    if N % 2:
        n = N//2 + 1
    else:
        n = N // 2
    li1 = li[:n]
    li2 = li[n:]
    total = []
    while len(total) < N:
        total.append(li1.pop(0))
        if len(total) != N and len(li2) == 0:
            continue
        elif len(total) != N and len(li2) != 0:
            total.append(li2.pop(0))
        elif len(total) == N:
            break
    print('#{}'.format(tc), end=" ")
    for i in total:
        print(i, end=" ")
    print()