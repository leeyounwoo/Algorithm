from itertools import product

n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]

for com in product(numbers, repeat=m):
    for i in com:
        print(i, end=' ')
    print()
