import sys
sys.stdin = open('input.txt')

def sort_box(box):
    for i in range(len(box) - 1, 0, -1):
        for j in range(0, i):
            if box[j] > box[j + 1]:
                box[j], box[j + 1] = box[j + 1], box[j]
    return box

for tc in range(10):
    dump = int(input())
    box = list(map(int, input().split()))

    for i in range(dump):
        box = sort_box(box)
        box[0] += 1
        box[-1] -= 1
    box = sort_box(box)
    result = box[-1]-box[0]
    print('#{} {}'.format(tc + 1, result))


