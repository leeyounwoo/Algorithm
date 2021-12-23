import sys

sys.stdin = open('input.txt')
n, m = map(int, sys.stdin.readline().split())
key_number = {}
key_pokect = {}
for i in range(1, n+1):
    name = sys.stdin.readline().rstrip()
    key_pokect[name] = i
    key_number[i] = name
numbers = [str(i) for i in range(10)]
for _ in range(m):
    q = sys.stdin.readline().rstrip()
    if q[0] in numbers:
        print(key_number[int(q)])
    else:
        print(key_pokect[q])