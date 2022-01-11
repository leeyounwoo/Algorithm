import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(N):
        boxes.sort()
        boxes[-1] -= 1
        boxes[0] += 1

        if max(boxes) - min(boxes) <= 1:
            break

        # if N % 100:
        #     if max(boxes) - min(boxes) == 1:
        #         break
        # else:
        #     if max(boxes) == min(boxes):
        #         break

    print('#{} {}'.format(tc + 1, max(boxes) - min(boxes)))