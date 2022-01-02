import sys

sys.stdin = open('input.txt')
for T in range(int(input())):
    n = int(input())
    clothes = {}
    for _ in range(n):
        name, key = map(str, sys.stdin.readline().rstrip().split())
        if key not in clothes:
            clothes[key] = 1
        else:
            clothes[key] += 1
    ans = 1
    for key in clothes.keys():
        ans *= clothes[key] + 1
    print(ans-1)