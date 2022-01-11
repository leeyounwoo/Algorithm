import sys
sys.stdin = open('input.txt')

# sol2
def find_max_min_box(boxes):
    max_height = 0
    max_idx = 0
    min_height = 987654321
    min_idx = 0

    for i in range(len(boxes)):
        height = boxes[i]
        if height > max_height :
            max_height = height
            max_idx = i
        if height < min_height :
            min_height = height
            min_idx = i
    return max_idx, min_idx

T = 10
for tc in range(1, 1+T):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump):

        max_idx, min_idx = find_max_min_box(boxes)

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    max_idx, min_idx = find_max_min_box(boxes)
    result = boxes[max_idx] - boxes[min_idx]
    print('#{} {}'.format(tc, result))
