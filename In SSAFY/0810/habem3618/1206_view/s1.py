import sys
sys.stdin = open('input.txt')

for tc in range(10):
    n = int(input())
    buildings = list(map(int, input().split()))
    result = 0
    for i in range(2, n-2):
        temp = min(buildings[i] - buildings[i-1], buildings[i] - buildings[i-2], buildings[i] - buildings[i+1],
                   buildings[i] - buildings[i+2])

        result += temp if temp > 0 else 0

    print(f'#{tc+1} {result}')
