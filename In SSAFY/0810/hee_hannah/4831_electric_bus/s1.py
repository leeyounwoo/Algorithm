import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    a = [0]
    c = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    K, N, M = map(int, input().split())
    b = list(map(int, input().split()))
    charger = a + b
    count = 0
    for i in range(len(charger)):
        if i+1 < len(charger) and c[charger[i+1]] - c[charger[i]] < K:
            count += 1
        elif i+1 < len(charger) and c[charger[i+1]] - c[charger[i]] <= (K//2):
            count -= 1
        elif i+1 < len(charger) and c[charger[i+1]] - c[charger[i]] > K:
            count = 0
            break
    print('#{} {}'.format(tc, count))


