import sys
sys.stdin = open('input.txt')

def permutation(total):
    global factory, min_cost

    if total > min_cost:
        return

    if len(factory) == N:
        min_cost = min(min_cost, total)
        return
    else:
        for i in range(N):
            if i not in factory:
                factory.append(i)
                permutation(total + cost[len(factory)-1][factory[-1]])
                factory.pop()

T = int(input())

for t in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    factory = []

    min_cost = float('inf')
    permutation(0)
    
    print('#{} {}'.format(t, min_cost))