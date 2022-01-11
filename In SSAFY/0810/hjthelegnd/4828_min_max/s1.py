import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    case = input()
    numbers = list(map(int, input().split()))
    result = max(numbers) - min(numbers)

    print('#{0} {1}'.format(tc, result))