import sys
sys.stdin = open("input.txt")
T = 10
for tc in range(1, T+1):
    N = int(input())
    count = 0
    magnetic = [list(map(int, input().split())) for _ in range(N)]
    for i in range(len(magnetic[0])):
        for j in range(len(magnetic)):
            if magnetic[i][j] == 1:
                for m in range(i, N):
                    if magnetic[m][j] == 0:
                        magnetic[i][j] = 0
                        count += 1
    print(count)