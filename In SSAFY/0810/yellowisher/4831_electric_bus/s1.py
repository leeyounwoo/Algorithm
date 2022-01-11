import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    location = 0
    move = K
    charge_count = 0
    while True:
        if move == 0:
            charge_count = 0
            break

        if location + move in arr:
            location += move
            charge_count += 1
            move = K

        elif location + K >= N:
            break
        else:
            move -= 1
    print("#%d %d"%(tc+1, charge_count))