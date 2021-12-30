import sys
def input():
    return sys.stdin.readline().rstrip()

sys.stdin = open('input.txt')
n, money = map(int, input().split())
kind = [int(input()) for _ in range(n)]
ans = 0
while money:
    flag = kind.pop()
    cnt, money = divmod(money, flag)
    ans += cnt

print(ans)
