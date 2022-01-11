import sys
sys.stdin = open('input.txt')
def dfs(idx):
    global result, charge

    if idx >= len(bus):
        if result >= charge:
            result = charge
        return

    if result <= charge:
        return

    for i in range(idx + bus[idx], idx, -1):
        charge += 1
        dfs(i)
        charge -= 1

T = int(input())
for tc in range(1, T+1):
    bus = list(map(int, input().split()))
    num = bus[0]
    result = 100000
    charge = 0
    dfs(1)

    print('#{} {}'.format(tc, result-1))