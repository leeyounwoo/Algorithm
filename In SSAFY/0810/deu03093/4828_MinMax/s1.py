import sys

sys.stdin = open('input.txt')

for T in range(1, int(input()) + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(T, max(numbers) - min(numbers)))