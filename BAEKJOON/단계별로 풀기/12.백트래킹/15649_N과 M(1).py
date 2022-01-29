from itertools import permutations

n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]
for com in permutations(numbers, m):
    for i in com:
        print(i, end=' ')
    print()