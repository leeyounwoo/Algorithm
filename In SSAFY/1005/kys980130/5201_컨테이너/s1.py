import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    box = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    box.sort()
    box.reverse()
    total = 0
    for i in range(len(truck)):
        for j in range(len(box)):
            if truck[i] >= box[j]:
                total += box[j]
                box.remove(box[j])
                break
    print('#{} {}'.format(tc, total))