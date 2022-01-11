from itertools import combinations
import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    tower = []
    for i in range(1, N+1):
        for combo in combinations(height, i):
            tower.append(sum(combo))
    
    tower.sort()
    for j in range(len(tower)):
        if tower[j] >= B:
            answer = tower[j] - B
            break
    
    print('#{} {}'.format(t, answer))