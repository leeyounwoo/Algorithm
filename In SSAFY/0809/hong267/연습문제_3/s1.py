import sys

sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    N = int(input())
    boxes = list(map(int, input().split()))

    block = 0
    for i in range(len(boxes)-1):
        tmp = 0
        for j in range(i, len(boxes)):
            if boxes[i] > boxes[j]:
                tmp += 1
        if tmp > block:
            block = tmp

    print(block)
