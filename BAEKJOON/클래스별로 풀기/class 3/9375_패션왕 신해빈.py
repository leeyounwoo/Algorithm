import sys
from itertools import combinations

sys.stdin = open('input.txt')
for T in range(int(input())):
    n = int(input())
    clothes = {}
    for _ in range(n):
        name, key = map(str, sys.stdin.readline().rstrip().split())
        if key not in clothes:
            clothes[key] = [name]
        elif name not in clothes[key]:
            clothes[key].append(name)
    clothes_keys = list(clothes.keys())
    print(clothes)