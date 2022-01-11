import sys
sys.stdin = open('input.txt')
from itertools import combinations

t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    a = n//2 # a개 만큼 요리하나에 써야
    n_list = []
    for i in range(1, n+1):
        n_list.append(i)
    b = combinations(range(1, n+1), a)
    total = []
    for i in b: # (1,2) -> 0,1 1,0으로,, 1234   012    01 02 10  12 20 21
        i = list(i)
        j = list(set(n_list) - set(i))
        food_a = 0
        food_b = 0
        for x in range(len(i)): # 0123 00 01 02 03 10 11 12 13 20 21 22 23 30 31 32 33
            for y in range(len(i)):
                if x != y:
                    food_a += li[i[x]-1][i[y]-1]
        for x in range(len(j)): # 0123 00 01 02 03 10 11 12 13 20 21 22 23 30 31 32 33
            for y in range(len(j)):
                if x != y:
                    food_b += li[j[x]-1][j[y]-1]
        total.append(abs(food_a-food_b))
    print(min(total))
