import sys
sys.stdin = open('input.txt')
N = int(input())
for tc in range(N):
    number = int(input())
    boxes = list(map(int, input().split()))
    max_box = 0
    for box in boxes:
        if box > max_box:
            max_box = box
    idx = []
    for i in range(number-1):
        if boxes[i] == max_box:
            idx.append(i)
    if len(idx) > 1:
        print(idx[1]-idx[0])
