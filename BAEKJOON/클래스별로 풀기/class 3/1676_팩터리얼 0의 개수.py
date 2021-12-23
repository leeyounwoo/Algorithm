import sys

sys.stdin = open('input.txt')
n = int(input())
num = 1
while n >= 1:
    num *= n
    n -= 1
ans = 0
num = str(num)
for i in range(len(num)-1, -1, -1):
    if num[i] != '0':
        break
    else:
        ans += 1
print(ans)