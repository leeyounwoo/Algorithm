import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, 11):
    numbers = int(input())
    building = list(map(int, input().split()))
    result = 0
    for i in range(2, numbers-1):
        for j in range(1, building[i]+1):
            if j > building[i-1] and j > building[i-2] and j > building[i+1] and j > building[i+2]:
                result += 1

    print('#{0} {1}'.format(tc, result))