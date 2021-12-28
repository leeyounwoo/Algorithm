import sys

sys.stdin = open('input.txt')

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
ans = 0
for i in range(n):
    ans += numbers[i] * (n-i)
print(ans)