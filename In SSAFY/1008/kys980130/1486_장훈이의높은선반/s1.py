import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    height.sort(reverse=True)
    total = 0
    result = 10000
    idx = 0
    result_lst = []
    for i in range(N-1):
        total = 0
        if height[i] >= B:
            if height[i]-B >= 0:
                result_lst.append(height[i]-B)

        else:
            total += height[i]
            for j in range(i+1, N):
                total += height[j]
                if total-B >= 0:
                    result_lst.append(total-B)
                    total -= height[j]

    print('#{} {}'.format(tc, min(result_lst)))