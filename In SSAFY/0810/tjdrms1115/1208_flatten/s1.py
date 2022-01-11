import sys
sys.stdin = open('input.txt')

def find_minmax(boxes):

    tempmin = 1000
    tempmax = 0
    for i in boxes:
        if tempmin > i:
            tempmin = i
        if tempmax < i:
            tempmax = i

    return tempmin, tempmax

T = 10

answer = []
for tc in range(1, T + 1):

    N = int(input())
    boxes = list(map(int, input().split()))

    result = 0

    for _ in range(N):
        # box_min = min(boxes)
        # box_max = max(boxes)
        box_min, box_max = find_minmax(boxes)
        if box_max - box_min > 1:
            boxes[boxes.index(box_min)] += 1
            boxes[boxes.index(box_max)] -= 1
        else:
            break

    box_min, box_max = find_minmax(boxes)
    result = box_max - box_min

    answer.append(result)

for tc in range(1, T + 1):
    print('#{0} {1}'.format(tc, answer[tc-1]))