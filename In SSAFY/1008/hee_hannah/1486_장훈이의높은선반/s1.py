import sys
sys.stdin = open('input.txt')
from itertools import combinations

# 런타임에러! 임포트 안하고도 풀어보기
t = int(input())

for tc in range(1, t+1):
    n, b = map(int, input().split()) # b <= sum(li)
    li = list(map(int, input().split()))
    a = []
    # 부분집합구하기..
    for i in range(0, len(li)+1):
        c = combinations(li, i)
        a.extend(c)
    fin = []
    for i in a:
        fin.append(sum(i))
    fin.sort()
    for i in fin:
        if i >= b:
            print('#{} {}'.format(tc, i-b))
            break