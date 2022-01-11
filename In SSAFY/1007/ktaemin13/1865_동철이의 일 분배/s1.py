import sys
sys.stdin = open('input.txt')

def workpower(result, person):
    global max_result
    global visited
    if result <= max_result:
        return
    if person == N:
        if max_result <= result:
            max_result = result
        return
    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            workpower(result*arr[person][j]*0.01, person+1)
            visited[j] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_result = 0
    workpower(1, 0)
    final_result = format(max_result*100, '.6f')
    print('#{} {:.6f}'.format(t, max_result*100))
