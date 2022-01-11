import sys
sys.stdin = open('input.txt')

for tc in range(10):
    cnt = int(input())
    box = list(map(int, input().split()))
    while cnt:
        box.sort()
        box[0] += 1
        box[-1] -= 1
        cnt -= 1
    box.sort()

    print('#{} {}'.format(tc+1, box[-1] - box[0]))

for tc in range(10):
    cnt = int(input()) + 1
    boxs = list(map(int, input().split()))
    max_idx, min_idx = 0, 0

    while cnt:
        for i in range(len(boxs)):
            if boxs[i] > boxs[max_idx]:
                max_idx = i
            if boxs[i] < boxs[min_idx]:
                min_idx = i
        if cnt == 1:
            break
        boxs[min_idx] += 1
        boxs[max_idx] -= 1
        cnt -= 1
    print(f'#{tc+1} {boxs[max_idx] - boxs[min_idx]}')
