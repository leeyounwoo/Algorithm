import sys
sys.stdin = open('input.txt')

def finding_entrance(start):

    i = 99
    j = start
    while i > 0:
        i -= 1
        if ladder[i][j-1] == 1:
            while j > 0 and ladder[i][j-1] == 1:
                j -= 1

        elif j < 99 and ladder[i][j+1] == 1:
            while j < 99 and ladder[i][j+1] == 1:
                j += 1
    return j

t = 10
for tc in range(1, t+1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    goal = 0
    for i in range(100):
        if ladder[99][i] == 2:
            goal = i
    ans = finding_entrance(goal)

    print(ans)