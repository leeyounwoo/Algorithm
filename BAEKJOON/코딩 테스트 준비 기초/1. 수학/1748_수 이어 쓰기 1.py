import sys

def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
n = input()
ans = 0
for i in range(1, len(n)):
    ans += 9 * i * (10 ** (i-1))
temp = len(n) - 1
if temp:
    ans += (int(n) - int('9' * (len(n) - 1))) * len(n)
    print(ans)
else:
    print(n)
