import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    dump = int(input()) # 덤프 시행 수
    boxes = list(map(int, input().split()))
    # 1 3 5 1 10 2 ...

    for _ in range(dump):
        # 1. 가장 높이가 높은 박스 찾기
        # 2. 가장 높이가 낮은 박스 찾기
        max_height = 0
        max_idx = 0

        min_height = 100
        min_idx = 0
        for i in range(len(boxes)):
            height = boxes[i]
            if height > max_height:
                max_height = height
                max_idx = i
            if height < min_height:
                min_height = height
                min_idx = i

        # 3. 찾은 인덱스를 이용해서
        # 최고 높이 박스  - 1
        # 최저 높이 박스  + 1

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    min_height = 100
    min_idx = 0
    for i in range(len(boxes)):
        height = boxes[i]
        if height > max_height:
            max_height = height
            max_idx = i
        if height < min_height:
            min_height = height
            min_idx = i
    result = boxes[max_idx] - boxes[min_idx]
    print('#{} {}'.format(tc, result))